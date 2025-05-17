import re

def extract_genus_species(tree_string):
    """
    Step 1: Extract only the genus, species, and optional subspecies, removing accession numbers.
    """
    print("Starting Step 1: Extracting genus and species identifiers...")

    # Regular expression to match the full identifier and isolate genus + species
    pattern = re.compile(r'([A-Z0-9]+\.[0-9]+_)([A-Z][a-z]+(?:_[a-z]+)*(?:_[a-z]+)*)')
    
    # Find all matches of genus and species in the string
    matches = pattern.findall(tree_string)
    
    print(f"Found {len(matches)} matches to clean...")

    # Set to store replacements
    unique_matches = set()

    # Process each match and replace in the string
    for match in matches:
        full_match = match[0] + match[1]
        if full_match not in unique_matches:
            unique_matches.add(full_match)
            # Replace only the exact match, not recursive
            tree_string = tree_string.replace(full_match, match[1])

    print("Step 1 complete.")
    return tree_string


def remove_metadata(tree_string):
    """
    Step 2: Remove any metadata trailing the genus and species.
    """
    print("Starting Step 2: Removing metadata...")

    # Regex to match metadata after species name, but stop at the colon
    metadata_pattern = re.compile(
        r'(_voucher|_isolate|_strain|_clone|_bio-material|_gene|_small_subunit|_large_subunit'
        r'|_internal_transcribed_spacer|_18S|_28S|_5.8S|_ITS|_region|_\d+|_[A-Z]{2,})[^:]*'
    )

    # Replace all instances with an empty string
    tree_string = re.sub(metadata_pattern, '', tree_string)

    print("Step 2 complete.")
    return tree_string


def clean_newick_tree(input_file, output_file):
    """
    Cleans the identifiers in a Newick tree file by:
    1. Extracting the genus and species.
    2. Removing any metadata trailing the genus and species.
    3. Preserving parentheses and branch lengths.
    """
    print(f"Processing file: {input_file}")
    
    # Read the entire Newick tree as one string
    with open(input_file, 'r') as file:
        tree_string = file.read()

    # Step 1: Extract genus and species
    tree_string = extract_genus_species(tree_string)

    # Step 2: Remove metadata but preserve branch lengths
    tree_string = remove_metadata(tree_string)

    # Ensure no newlines were added
    tree_string = tree_string.replace("\n", "")

    # Write the cleaned tree back as a single line
    with open(output_file, 'w') as file:
        file.write(tree_string)

    print(f"Newick tree cleaned and saved to: {output_file}")


if __name__ == "__main__":
    import argparse

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Clean Newick tree identifiers.")
    parser.add_argument('input_file', type=str, help='Path to the input Newick tree file.')
    parser.add_argument('output_file', type=str, help='Path to save the cleaned Newick tree file.')
    
    args = parser.parse_args()
    
    # Run the cleaning process
    clean_newick_tree(args.input_file, args.output_file)
