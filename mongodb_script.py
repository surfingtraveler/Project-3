import pandas as pd
from pymongo import MongoClient
import os

# Load the CSV file
csv_file = "global-shark-attack_cleaned_for_columns.csv"
data = pd.read_csv(csv_file)

# Function to preprocess the data and replace na's with empty stringmong
def preprocess_data(data):
    data = data.fillna("")  
    return data

# Function to insert data into db
def insert_data_into_mongodb(data):
    # Establish the MongoDB connection
    client = MongoClient('mongodb://localhost:27017/')

    # Connect to the sharks db and attacks collection
    db = client.sharks_db
    collection = db.attacks

    # Convert dataFrame records to dictionary and insert into collection
    records = data.to_dict(orient='records')
    collection.insert_many(records)

    print("Data inserted into MongoDB successfully.")

if __name__ == "__main__":
    # Preprocess the data before inserting into Mongo db
    data = preprocess_data(data)

    # Insert data into Mongodb
    insert_data_into_mongodb(data)
