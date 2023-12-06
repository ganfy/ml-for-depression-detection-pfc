
import os
import pandas as pd
from glob import glob

categories = ['Nondepressed', 'Mild', 'Moderate', 'Moderately Severe', 'Severe']

for category in categories:
    category_folder = f'DAIC_WOZ/train/{category}'  # Replace with the actual path to the category folder
    
    # Get the list of filenames matching the pattern '*TRANS*.csv' in the category folder
    files = glob(os.path.join(category_folder, '*TRANS*.csv'))
    print(len(files))
    for file in files:
        # Read the CSV file
        df = pd.read_csv(file, sep='\t')
        
        # Filter rows where 'speaker' is "Participant" and keep only the 'value' column
        result_df = df.loc[df['speaker'] == 'Participant', ['value']]

        # Overwrite the original CSV file with the modified DataFrame
        result_df.to_csv(file, index=False, sep='\t')


for category in categories:
    category_folder = f'DAIC_WOZ/test/{category}'  # Replace with the actual path to the category folder
    print(category_folder)
    # Get the list of filenames matching the pattern '*TRANS*.csv' in the category folder
    files = glob(os.path.join(category_folder, '*TRANS*.csv'))
    print(len(files))
    for file in files:
        # Read the CSV file
        df = pd.read_csv(file, sep='\t')
        
        # Filter rows where 'speaker' is "Participant" and keep only the 'value' column
        result_df = df.loc[df['speaker'] == 'Participant', ['value']]

        # Overwrite the original CSV file with the modified DataFrame
        result_df.to_csv(file, index=False, sep='\t')