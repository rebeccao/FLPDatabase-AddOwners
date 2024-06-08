import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB URI from environment variables
mongodb_uri = os.getenv('MONGODB_URI')

if not mongodb_uri:
  raise ValueError("MONGODB_URI is not set in the environment variables")

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client.poetDB
collection = db.Poet

# Fetch all data from MongoDB
cursor = collection.find()
data = list(cursor)

print(f"Number of records fetched: {len(data)}")

df = pd.DataFrame(data)

# Export to CSV
df.to_csv('mongodb_export.csv', index=False)
