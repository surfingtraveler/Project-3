import csv
from pymongo import MongoClient

# Establish the MongoDB connection
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    return client

# Connect to database and collection
def get_sharks_collection():
    client = get_mongo_connection()
    db = client.sharks_db  
    collection = db.attacks
    return collection

# Clean/replace null values with "Unknown" and add to our database
def insert_data_from_csv(csv_file):
    collection = get_sharks_collection()

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                if value.strip() == "":
                    row[key] = "Unknown"

                # Convert Latitude and Longitude fields to float
                if key == "latitude" or key == "longitude":
                    try:
                        row[key] = float(value)
                    except ValueError:
                        row[key] = 0.0

            # Insert data into our database
            collection.insert_one(row)

    print("Data from CSV successfuly inserted into the database.")

if __name__ == "__main__":
    csv_file = "global-shark-attack_updated_for_LAT_LONG.csv"
    insert_data_from_csv(csv_file)
