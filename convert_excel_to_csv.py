import pandas as pd

# Load the Excel file
excel_file = 'poetDB-small1.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file)

# Save to CSV
csv_file = 'poetDB-small1.csv'
df.to_csv(csv_file, index=False)

print(f"File converted to {csv_file}")