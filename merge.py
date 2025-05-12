import pandas as pd

def merge_spore_data(info_path, data_path, output_path):
    # Load the datasets
    spore_info_df = pd.read_csv(info_path)
    spore_data_df = pd.read_csv(data_path)
    
    # Reassign proper column names and clean up the Excel file
    spore_info_df.columns = spore_info_df.iloc[2]
    spore_info_df = spore_info_df[3:]
    spore_info_df.rename(columns=lambda x: x.strip(), inplace=True)
    
    # Merge the two datasets based on species name
    merged_df = pd.merge(spore_info_df, spore_data_df, how='left', left_on='species', right_on='species')
    
    # Save the merged DataFrame to CSV
    merged_df.to_csv(output_path, index=False)
    print(f"Merged data saved to {output_path}")

if __name__ == "__main__":
    # Define file paths
    info_path = 'Spore_info_all.csv'
    data_path = 'Sporelengthwidthvolume.csv'
    output_path = 'Spore_info_all_merged.csv'
    
    # Call the merge function
    merge_spore_data(info_path, data_path, output_path)
# This script merges two datasets: one containing spore information and another containing spore data.
