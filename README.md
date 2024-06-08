# FindLostPoets MongoDB Update Scripts

This repository contains the necessary Python scripts to update the FINDLOSTPOETS MongoDB with Manifold's LostPoets metadata.

## Fetch the Manifold LostPoets Metadata

### Scripts
- `fetch-manifold-poets.py`
- `manifoldData.py`
- `progress.txt`

### Output
- `ManifoldLPsddMMMyy.xlsx`

### Description
`fetch-manifold-poets.py` uses the Manifold API to loop through the 28,170 LostPoets to fetch their metadata, as defined by `manifoldData.py`. The data is saved to an Excel file.

If a network error causes the loop to exit early, the last successful index is saved to a file called `progress.txt`. The next time the script is run, it will start from that index to continue writing the metadata to the Excel file.

### Run the Script
In a Mac environment, use `caffeinate` to prevent Sleep mode from halting the script:

`caffeinate -i python3 fetch-manifold-poets.py`

## Export FINDLOSTPOETS MongoDB (poetsDB)
 
### Script
- `fetch-mongodb.py`

### Output
- `mongo_export.csv`

### Description
This script connects to the poetsDB MongoDB, fetches it into a Panda DataFrame then exports it to a .csv file. 

### Run the Script
`python fetch_mongodb.py`

## Merge the data and create a new poetDB.json file

### Script
- `convert_excel_to_json.py`
### Output
- `poetDB.json`

### Description
Open the mongo csv file in Excel and manually merge the data from the manifold Excel file. Run this script to convert the Excel file in a json file that will be imported into MongoDB.

### Run the Script
`python convert_excel_to_json.py`

## Import poetsDB.json to MongoDB

### Description
This command imports the new .json file into MongoDB

### Terminal command line
`mongoimport --uri "mongodb_uri" --collection Poet --type json --file poetDB.json --verbose`
