import json
from pymongo import MongoClient

# Establish the MongoDB connection
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    return client

# Connect to the 'sharks' database and 'attacks' collection
def get_sharks_collection():
    client = get_mongo_connection()
    db = client.sharks_db  
    collection = db.attacks
    return collection

# Load data from JSON file
def load_data_from_json(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

# Replace null values with "Unknown" and insert data into the mongo database
def insert_data_from_json():
    collection = get_sharks_collection()
    json_data = load_data_from_json("global_shark_attacks.json")

    for item in json_data:
        for key, value in item.items():
            if value is None:
                item[key] = "Unknown"

    # Insert data into the mongo database
    if json_data:
        result = collection.insert_many(json_data)
        print(f"{len(result.inserted_ids)} valid data entries inserted into the database.")
    else:
        print("No valid data to insert.")

if __name__ == "__main__":
    insert_data_from_json()





