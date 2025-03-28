#!/bin/bash

my_array=(3 4 5 6 7)

mkdir -p ./RawData/GB_fa

for i in "${my_array[@]}"; do
    NAME=$(head -n 1 "$1" | cut -d "," -f "$i")
    tail -n +2 "$1" | while IFS= read -r LINE; do
        acc=$(echo "$LINE" | cut -d "," -f "$i")
        if [[ -n "$acc" ]]; then
            echo "Fetching $acc for $NAME"
            efetch -db nucleotide -id "$acc" -format fasta >> "./RawData/GB_fa/${NAME}.fasta"
        fi
    done
done
