from flask import Flask, jsonify, request
from pymongo import MongoClient

#Create an instance of Flask to pass __name__
app = Flask(__name__)

# Establish the MongoDB connection
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    return client

# Connect to the 'sharks' database and created collection 'attacks'
def get_sharks_collection():
    client = get_mongo_connection()
    db = client.sharks_db  # Change 'sharks' to the appropriate database name
    collection = db.attacks
    return collection

@app.route("/", methods=['GET'])
def get_all_data():
    collection = get_sharks_collection()
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    collection = get_sharks_collection()
    collection.insert_one(new_data)

if __name__ == '__main__':
    app.run(debug=True)



