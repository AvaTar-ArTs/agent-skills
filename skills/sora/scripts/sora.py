#!/usr/bin/env python3
"""
Sora Video Generation CLI for Hermes Agent
Handles video creation, remixing, polling, and downloading via OpenAI's Sora API
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any

import openai
from openai import OpenAI


def setup_openai():
    """Setup OpenAI client with API key from environment"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
        print("Please set your OpenAI API key:", file=sys.stderr)
        print("  export OPENAI_API_KEY='your-key-here'", file=sys.stderr)
        sys.exit(1)
    
    return OpenAI(api_key=api_key)


def cmd_create(args, client: OpenAI):
    """Create a new video generation job"""
    # Build the prompt
    prompt_parts = [args.prompt]
    
    if args.use_case:
        prompt_parts.insert(0, f"Use case: {args.use_case}")
    if args.scene:
        prompt_parts.append(f"Scene/background: {args.scene}")
    if args.subject:
        prompt_parts.append(f"Subject: {args.subject}")
    if args.action:
        prompt_parts.append(f"Action: {args.action}")
    if args.camera:
        prompt_parts.append(f"Camera: {args.camera}")
    if args.lighting_mood:
        prompt_parts.append(f"Lighting/mood: {args.lighting_mood}")
    if args.color_palette:
        prompt_parts.append(f"Color palette: {args.color_palette}")
    if args.style_format:
        prompt_parts.append(f"Style/format: {args.style_format}")
    if args.timing_beats:
        prompt_parts.append(f"Timing/beats: {args.timing_beats}")
    if args.audio:
        prompt_parts.append(f"Audio: {args.audio}")
    if args.text:
        prompt_parts.append(f'Text (verbatim): "{args.text}"')
    if args.dialogue:
        prompt_parts.append("Dialogue:")
        prompt_parts.append(f'- Speaker: "{args.dialogue}"')
    if args.constraints:
        prompt_parts.append(f"Constraints: {args.constraints}")
    if args.avoid:
        prompt_parts.append(f"Avoid: {args.avoid}")
    
    prompt = "\n".join(prompt_parts)
    
    # If we have a prompt file, use it instead
    if args.prompt_file:
        with open(args.prompt_file, 'r') as f:
            prompt = f.read().strip()
    
    # Prepare parameters
    params = {
        "model": args.model,
        "prompt": prompt,
        "size": args.size,
        "seconds": str(args.seconds),  # API expects string
    }
    
    if args.variant:
        params["variant"] = args.variant
    
    print(f"Creating video generation job...")
    print(f"Model: {args.model}")
    print(f"Size: {args.size}")
    print(f"Duration: {args.seconds} seconds")
    if not args.no_augment or args.prompt_file:
        print(f"Prompt: {prompt[:200]}{'...' if len(prompt) > 200 else ''}")
    
    try:
        response = client.videos.generate(**params)
        job_id = response.id
        print(f"Job created successfully!")
        print(f"Job ID: {job_id}")
        print(f"Status: {response.status}")
        
        # Save job ID if requested
        if args.save_job_id:
            with open(args.save_job_id, 'w') as f:
                f.write(job_id)
            print(f"Job ID saved to: {args.save_job_id}")
        
        # Auto-poll if requested
        if args.poll:
            cmd_poll(type('Args', (), {
                'job_id': job_id,
                'interval': args.interval,
                'timeout': args.timeout,
                'output_dir': args.output_dir,
                'download': True,
                'verbose': args.verbose
            })(), client)
            
    except Exception as e:
        print(f"Error creating video: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_remix(args, client: OpenAI):
    """Remix an existing video"""
    params = {
        "model": args.model,
        "prompt": args.prompt,
        "video_id": args.video_id,
        "size": args.size,
        "seconds": str(args.seconds),
    }
    
    if args.variant:
        params["variant"] = args.variant
    
    print(f"Remixing video {args.video_id}...")
    print(f"Model: {args.model}")
    print(f"Size: {args.size}")
    print(f"Duration: {args.seconds} seconds")
    print(f"Prompt: {args.prompt[:200]}{'...' if len(args.prompt) > 200 else ''}")
    
    try:
        response = client.videos.generate(**params)
        job_id = response.id
        print(f"Remix job created successfully!")
        print(f"Job ID: {job_id}")
        print(f"Status: {response.status}")
        
        if args.save_job_id:
            with open(args.save_job_id, 'w') as f:
                f.write(job_id)
            print(f"Job ID saved to: {args.save_job_id}")
            
        if args.poll:
            cmd_poll(type('Args', (), {
                'job_id': job_id,
                'interval': args.interval,
                'timeout': args.timeout,
                'output_dir': args.output_dir,
                'download': True,
                'verbose': args.verbose
            })(), client)
            
    except Exception as e:
        print(f"Error remixing video: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_status(args, client: OpenAI):
    """Check status of a video job"""
    try:
        response = client.videos.retrieve(args.job_id)
        print(f"Job ID: {response.id}")
        print(f"Status: {response.status}")
        print(f"Model: {response.model}")
        print(f"Created at: {response.created_at}")
        
        if hasattr(response, 'error') and response.error:
            print(f"Error: {response.error}")
            
        if response.status in ['completed', 'failed', 'cancelled']:
            if hasattr(response, 'video') and response.video:
                print(f"Video URL: {response.video.url}")
                if hasattr(response.video, 'thumbnail_url') and response.video.thumbnail_url:
                    print(f"Thumbnail URL: {response.video.thumbnail_url}")
                if hasattr(response.video, 'spritesheet_url') and response.video.spritesheet_url:
                    print(f"Spritesheet URL: {response.video.spritesheet_url}")
                    
    except Exception as e:
        print(f"Error retrieving job status: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_poll(args, client: OpenAI):
    """Poll a job until completion"""
    start_time = time.time()
    
    while True:
        # Check timeout
        if args.timeout and (time.time() - start_time) > args.timeout:
            print(f"Timeout reached ({args.timeout}s)", file=sys.stderr)
            sys.exit(1)
        
        try:
            response = client.videos.retrieve(args.job_id)
            status = response.status
            
            if args.verbose:
                print(f"[{time.strftime('%H:%M:%S')}] Status: {status}")
            
            if status == 'completed':
                print(f"Job completed successfully!")
                if hasattr(response, 'video') and response.video:
                    print(f"Video URL: {response.video.url}")
                    if args.download:
                        download_assets(response.video, args.output_dir, args.verbose)
                break
            elif status in ['failed', 'cancelled']:
                print(f"Job {status}!")
                if hasattr(response, 'error') and response.error:
                    print(f"Error: {response.error}")
                sys.exit(1)
            elif status in ['in_progress', 'queued']:
                # Continue polling
                time.sleep(args.interval)
            else:
                print(f"Unknown status: {status}")
                time.sleep(args.interval)
                
        except Exception as e:
            print(f"Error polling job: {e}", file=sys.stderr)
            sys.exit(1)


def download_assets(video_obj, output_dir: str, verbose: bool = False):
    """Download video and related assets"""
    import requests
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Download video
    if hasattr(video_obj, 'url') and video_obj.url:
        if verbose:
            print(f"Downloading video from {video_obj.url}")
        try:
            resp = requests.get(video_obj.url, stream=True, timeout=30)
            resp.raise_for_status()
            video_file = output_path / "video.mp4"
            with open(video_file, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Video saved to: {video_file}")
        except Exception as e:
            print(f"Error downloading video: {e}", file=sys.stderr)
    
    # Download thumbnail
    if hasattr(video_obj, 'thumbnail_url') and video_obj.thumbnail_url:
        if verbose:
            print(f"Downloading thumbnail from {video_obj.thumbnail_url}")
        try:
            resp = requests.get(video_obj.thumbnail_url, timeout=10)
            resp.raise_for_status()
            thumb_file = output_path / "thumbnail.jpg"
            with open(thumb_file, 'wb') as f:
                f.write(resp.content)
            print(f"Thumbnail saved to: {thumb_file}")
        except Exception as e:
            print(f"Error downloading thumbnail: {e}", file=sys.stderr)
    
    # Download spritesheet
    if hasattr(video_obj, 'spritesheet_url') and video_obj.spritesheet_url:
        if verbose:
            print(f"Downloading spritesheet from {video_obj.spritesheet_url}")
        try:
            resp = requests.get(video_obj.spritesheet_url, timeout=10)
            resp.raise_for_status()
            sprite_file = output_path / "spritesheet.jpg"
            with open(sprite_file, 'wb') as f:
                f.write(resp.content)
            print(f"Spritesheet saved to: {sprite_file}")
        except Exception as e:
            print(f"Error downloading spritesheet: {e}", file=sys.stderr)


def cmd_list(args, client: OpenAI):
    """List recent video jobs"""
    try:
        # Note: Sora API might not have a list endpoint, this is placeholder
        print("Listing not implemented for Sora API - use job IDs directly")
        print("Tip: Save job IDs with --save-job-id when creating/remixing")
    except Exception as e:
        print(f"Error listing jobs: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_download(args, client: OpenAI):
    """Download assets for a completed job"""
    try:
        response = client.videos.retrieve(args.job_id)
        if response.status != 'completed':
            print(f"Job is not completed (status: {response.status})", file=sys.stderr)
            sys.exit(1)
        
        if not hasattr(response, 'video') or not response.video:
            print("No video available for this job", file=sys.stderr)
            sys.exit(1)
        
        print(f"Downloading assets for job {args.job_id}...")
        download_assets(response.video, args.output_dir, args.verbose)
        
    except Exception as e:
        print(f"Error downloading assets: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Sora Video Generation CLI for Hermes Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new video')
    create_parser.add_argument('prompt', help='Text prompt for video generation')
    create_parser.add_argument('--prompt-file', help='Read prompt from file instead')
    create_parser.add_argument('--use-case', help='Where the clip will be used')
    create_parser.add_argument('--scene', help='Scene/background description')
    create_parser.add_argument('--subject', help='Main subject')
    create_parser.add_argument('--action', help='Single clear action')
    create_parser.add_argument('--camera', help='Shot type, angle, motion')
    create_parser.add_argument('--lighting-mood', help='Lighting + mood')
    create_parser.add_argument('--color-palette', help='3-5 color anchors')
    create_parser.add_argument('--style-format', help='Film/animation/format cues')
    create_parser.add_argument('--timing-beats', help='Counts or beats for timing')
    create_parser.add_argument('--audio', help='Ambient cue / music / voiceover')
    create_parser.add_argument('--text', help='Exact on-screen text')
    create_parser.add_argument('--dialogue', help='Dialogue line')
    create_parser.add_argument('--constraints', help='Must keep/must avoid constraints')
    create_parser.add_argument('--avoid', help='Negative constraints')
    create_parser.add_argument('--model', default='sora-2', help='Model to use (default: sora-2)')
    create_parser.add_argument('--size', default='1280x720', help='Video size (default: 1280x720)')
    create_parser.add_argument('--seconds', type=int, default=4, choices=[4, 8, 12], help='Duration in seconds (default: 4)')
    create_parser.add_argument('--variant', help='Video variant')
    create_parser.add_argument('--no-augment', action='store_true', help='Skip prompt augmentation')
    create_parser.add_argument('--poll', action='store_true', help='Poll until completion')
    create_parser.add_argument('--interval', type=int, default=5, help='Polling interval in seconds (default: 5)')
    create_parser.add_argument('--timeout', type=int, help='Timeout in seconds')
    create_parser.add_argument('--output-dir', default='./sora-output', help='Output directory for downloads')
    create_parser.add_argument('--save-job-id', help='Save job ID to file')
    create_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    # Remix command
    remix_parser = subparsers.add_parser('remix', help='Remix an existing video')
    remix_parser.add_argument('video_id', help='ID of video to remix')
    remix_parser.add_argument('prompt', help='Text prompt for remix')
    remix_parser.add_argument('--model', default='sora-2', help='Model to use (default: sora-2)')
    remix_parser.add_argument('--size', default='1280x720', help='Video size (default: 1280x720)')
    remix_parser.add_argument('--seconds', type=int, default=4, choices=[4, 8, 12], help='Duration in seconds (default: 4)')
    remix_parser.add_argument('--variant', help='Video variant')
    remix_parser.add_argument('--poll', action='store_true', help='Poll until completion')
    remix_parser.add_argument('--interval', type=int, default=5, help='Polling interval in seconds (default: 5)')
    remix_parser.add_argument('--timeout', type=int, help='Timeout in seconds')
    remix_parser.add_argument('--output-dir', default='./sora-output', help='Output directory for downloads')
    remix_parser.add_argument('--save-job-id', help='Save job ID to file')
    remix_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Check status of a video job')
    status_parser.add_argument('job_id', help='Job ID to check')
    status_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List recent video jobs')
    list_parser.add_argument('--limit', type=int, default=10, help='Number of jobs to show')
    
    # Download command
    download_parser = subparsers.add_parser('download', help='Download assets for completed job')
    download_parser.add_argument('job_id', help='Job ID to download')
    download_parser.add_argument('--output-dir', default='./sora-output', help='Output directory for downloads')
    download_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Setup OpenAI client
    client = setup_openai()
    
    # Route to appropriate command handler
    if args.command == 'create':
        cmd_create(args, client)
    elif args.command == 'remix':
        cmd_remix(args, client)
    elif args.command == 'status':
        cmd_status(args, client)
    elif args.command == 'poll':
        cmd_poll(args, client)
    elif args.command == 'list':
        cmd_list(args, client)
    elif args.command == 'download':
        cmd_download(args, client)
    else:
        print(f"Unknown command: {args.command}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()