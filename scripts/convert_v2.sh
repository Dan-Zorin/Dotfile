#!/bin/bash

input_folder="./"
output_folder="new"

mkdir -p "$output_folder"

counter=1

for file in $(ls -v "$input_folder"/*.webp); do
    if [ -f "$file" ]; then
        output_file="$output_folder/${counter}.webp"

        echo "Converting $file to $output_file"
        cwebp -q 30 "$file" -o "$output_file"

        rm "$file"


        ((counter++))
    fi
done

cd new
mv * ../
cd ../

rmdir new

echo "Konverze a odstranění dokončeno."


