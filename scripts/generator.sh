COUNT=261+1

for ((i=1; i<COUNT; i++)); do
    printf "{\nimage: \"/galerie/31-zabavne-odpoledne-2017/${i}.webp\"\n},\n"
done > file.txt

