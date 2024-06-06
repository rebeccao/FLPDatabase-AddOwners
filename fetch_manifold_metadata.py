import requests
import pandas as pd
import time
import os

# Import the helper function for parsing the data
from manifoldData import parse_manifold_metadata

# Set up the base URL and headers for the API requests
url = "https://lostpoets.api.manifoldxyz.dev/metadata/"
headers = {
    "Accept": "application/json",  
}

# Initialize variables for the loop
num_of_poet_batches = 1565
limit = 18
progress_file = "progress.txt"

# Read the last successful batch index from the progress file
if os.path.exists(progress_file):
    with open(progress_file, 'r') as file:
        i = int(file.read().strip())
else:
    i = 0  # Start from the beginning if no progress file exists

#poet_counter = 1  # Start the poet_id from 1
rsp_array = []

# Fetch data from the API
while i <= num_of_poet_batches:
    print(f"Processing batch {i}...")

    j = 0
    while j < limit:
        poet_id = (i * limit) + j
        response = requests.get(url + str(poet_id), headers=headers)
        
        print(f"Fetching poet_id {poet_id} - Status code: {response.status_code}")
        
        if response.status_code != 200:
            if response.status_code == 404:
                print(f"404 error for poet_id {poet_id}")
                j += 1
                continue
            else:
                print(f"Error: response.status_code = {response.status_code}")
                break
        
        poet_json = response.json()
        
        rsp_array.append(poet_json)
        
        j += 1
    
    # Save progress
    with open(progress_file, 'w') as file:
        file.write(str(i))
    
    i += 1

# Parse the fetched data with incremental poet_id
print("Parsing fetched data...")
parsed_poets = [parse_manifold_metadata(poet, idx + 1) for idx, poet in enumerate(rsp_array)]

# Convert the parsed data to a DataFrame
poets_df = pd.DataFrame(parsed_poets)

# Remove the '_id' column if it exists
if '_id' in poets_df.columns:
    del poets_df['_id']

# Set the 'origin' column as the index of the DataFrame
origin_df = poets_df.set_index('origin')

# Generate a filename for the Excel file
filename = "ManifoldLPs" + time.strftime("%d%b%y", time.gmtime()) + ".xlsx"

# Save the DataFrame to an Excel file
origin_df.to_excel(filename)

# Print the total number of records saved
print(f"Total records saved: {len(poets_df)}")
