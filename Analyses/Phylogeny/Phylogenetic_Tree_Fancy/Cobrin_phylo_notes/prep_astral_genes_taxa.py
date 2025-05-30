import os
import pandas as pd
from Bio import SeqIO

# Define paths
fasta_dir = "./"  # Directory containing the FASTA files
csv_file = "./Accessions_automated_filled.csv"  # Path to the CSV file
mapping_output = "astral_mapping.txt"  # Output file for the mapping string
error_log = "error_log.txt"  # File to log errors

# Read CSV file into pandas DataFrame
df = pd.read_csv(csv_file)

# Create the output file and error log (empty it if it already exists)
with open(mapping_output, 'w') as mapping_file, open(error_log, 'w') as error_file:
    # Loop through each FASTA file in the directory
    for fasta_file in os.listdir(fasta_dir):
        if fasta_file.endswith(".fasta"):
            fasta_path = os.path.join(fasta_dir, fasta_file)

            # Extract the accession number from the FASTA header
            with open(fasta_path, 'r') as f:
                for record in SeqIO.parse(f, "fasta"):
                    accession = record.id.split("_")[0]  # Assuming the accession is the first part of the ID
                    
                    # Search for the corresponding taxa name in the entire CSV row
                    matching_rows = df[df.apply(lambda row: row.astype(str).str.contains(accession).any(), axis=1)]
                    
                    if len(matching_rows) == 0:
                        # No match found, log the error
                        error_file.write(f"Error: No match found for accession {accession} in file {fasta_file}\n")
                    elif len(matching_rows) > 1:
                        # Multiple matches found, log the error
                        error_file.write(f"Error: Multiple matches found for accession {accession} in file {fasta_file}\n")
                    else:
                        # Single match found, write the mapping
                        taxa_name = matching_rows.iloc[0]['Species_Name_in_dataset']
                        mapping_file.write(f"{accession}\t{taxa_name}\n")

print(f"Mapping string has been saved to {mapping_output}")