#!/bin/bash

readarray -t quickjumps < "$HOME/dmenuscripts/quickjumps.txt"

quickjumpslist=$(printf "%s\n" "${quickjumps[@]}" | awk '{print $1"   |   "$2}' | sort)

choice=$(printf "%s\n" "$quickjumpslist" | dmenu -l 10 -fn "Satoshi:semibold:size=13" -p "quickjumps:") "$@" || exit

path=$(echo "${choice}" | awk '{print $NF}') || exit
cd "$path" && alacritty
