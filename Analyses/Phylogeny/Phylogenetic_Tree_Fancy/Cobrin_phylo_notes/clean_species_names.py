import re

def clean_newick_tree(input_file, output_file):
    """
    Cleans the identifiers in a Newick tree file by extracting only the genus and species.

    Parameters:
    - input_file (str): Path to the input Newick tree file.
    - output_file (str): Path to save the cleaned Newick tree file.
    """
    # Regular expression to capture the genus and species from the identifier
    pattern = re.compile(r'_[A-Z][a-z]+_[a-z]+(?:_[a-z]+)*')

    # Read the lines from the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Process each line and replace the identifier
    cleaned_lines = []
    for line in lines:
        # Find all matches of genus and species in the line
        matches = pattern.findall(line)
        for match in matches:
            # Remove the leading underscore
            clean_name = match[1:]
            # Replace the original string in the line with the clean name
            line = line.replace(match, clean_name)
        cleaned_lines.append(line)

    # Write the cleaned lines to a new file
    with open(output_file, 'w') as file:
        file.writelines(cleaned_lines)

    print(f"Newick tree cleaned and saved to: {output_file}")


# Example usage:
clean_newick_tree('genes.trees', 'genes_cleaned.trees')