for file in *; do
    if [[ -f "$file" ]]; then
        echo "Processing $file..."
        iqtree2 -s "$file" --alrt 1000
    fi
done