import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
import os

# Create a Flask instance
app = Flask(__name__)
CORS(app)


# Load data from MongoDB database
def get_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client


def get_shark_attacks_collection():
    client = get_mongo_connection()
    db = client["shark_attacks"]
    collection = db["shark_frequencies"]
    return collection


# Route to serve the html file
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shark_attacks_data")
def get_shark_attacks_data():
    collection = get_shark_attacks_collection()
    pipeline = [
        {"$match": {"Year": {"$gte": 2018, "$lte": 2023}}},
        {"$group": {"_id": {"Year": "$Year", "Sex": "$Sex"}, "count": {"$sum": 1}}},
        {"$sort": {"_id.Year": 1, "_id.Sex": 1}},
    ]
    result = list(collection.aggregate(pipeline))
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
