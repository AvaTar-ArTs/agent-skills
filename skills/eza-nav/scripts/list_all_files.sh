#!/bin/bash
# Advanced file listing script using eza.
# Usage: ./list_all_files.sh [directory] [options]
# Options:
#   -t: Enable tree view
#   -d <depth>: Set tree depth (default 2)
#   -h: Show help

dir_path=${1:-.}
tree_view=false
depth=2

# Basic option parsing
shift
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t) tree_view=true ;;
        -d) depth="$2"; shift ;;
        -h) echo "Usage: $0 [directory] [-t] [-d depth]"; exit 0 ;;
    esac
    shift
done

# Build command based on flags
if [ "$tree_view" = true ]; then
    /usr/local/bin/eza -a -T -L "$depth" --git --icons --group-directories-first "$dir_path"
else
    /usr/local/bin/eza -a -l -H --git --icons --group-directories-first "$dir_path"
fi
