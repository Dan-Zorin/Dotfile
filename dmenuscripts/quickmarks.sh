#!/bin/bash

readarray -t quickmarks < "$HOME/dmenuscripts/quickmarks.txt"
quickmarkslist=$(printf "%s\n" "${quickmarks[@]}" | awk '{print $1" - "$NF}' | sort)

choice=$(printf "%s\n" "$quickmarkslist" | dmenu -l 10 -p "quickmarks:") "$@" || exit

url=$(echo "${choice}" | awk '{print $NF}') || exit
brave "$url"
