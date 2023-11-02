#!/bin/bash

input_folder="./galerie/31-zabavne-odpoledne-2017"
output_folder=$input_folder

mkdir -p "$output_folder"

counter=1

for file in "$input_folder"/*.jpg "$input_folder"/*.jpeg "$input_folder"/*.png "$input_folder"/*.gif; do
    if [ -f "$file" ]; then
        output_file="$output_folder/${counter}.webp"
        echo "Converting $file to $output_file"
        cwebp -q 100 "$file" -o "$output_file"
        
        rm "$file"
        
        ((counter++))
    fi
done

echo "Konverze a odstranění dokončeno."

