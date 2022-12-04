#!/bin/bash

readarray -t quickmarks < "$HOME/dmenuscripts/quickmarks.txt"

quickmarkslist=$(printf "%s\n" "${quickmarks[@]}" | awk '{print $1"   |   "$3}' | sort)

choice=$(printf "%s\n" "$quickmarkslist" | dmenu -l 10 -fn "Satoshi:semibold:size=13" -p "quickmarks:") "$@" || exit

url=$(echo "${choice}" | awk '{print $2}') || exit
brave "$url"
