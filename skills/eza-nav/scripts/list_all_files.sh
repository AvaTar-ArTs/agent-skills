#!/bin/bash
# Advanced file listing script using eza.
# Usage: ./list_all_files.sh [directory] [options]
# Options:
#   -t: Enable tree view
#   -d <depth>: Set tree depth (default 2)
#   -h: Show help

resolve_eza() {
    if command -v eza >/dev/null 2>&1; then
        command -v eza
        return 0
    fi
    local candidate
    for candidate in /opt/local/bin/eza /usr/local/bin/eza "$HOME/.local/bin/eza"; do
        if [ -x "$candidate" ]; then
            printf '%s\n' "$candidate"
            return 0
        fi
    done
    echo "eza-nav: eza not found (command -v eza, /opt/local/bin/eza, /usr/local/bin/eza)" >&2
    return 127
}

EZA=$(resolve_eza) || exit 127

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
    "$EZA" -a -T -L "$depth" --git --icons --group-directories-first "$dir_path"
else
    "$EZA" -a -l -H --git --icons --group-directories-first "$dir_path"
fi
