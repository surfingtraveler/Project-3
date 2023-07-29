import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pymongo import MongoClient
from collections import defaultdict
from datetime import datetime
import os
import dateutil.parser


# Create a Flask instance
app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client.shark_attacks
collection = db.shark_frequencies


def get_shark_attacks_collection():
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
        {
            "$group": {
                "_id": "$Year",
                "male_count": {"$sum": {"$cond": [{"$eq": ["$Sex", "M"]}, 1, 0]}},
                "female_count": {"$sum": {"$cond": [{"$eq": ["$Sex", "F"]}, 1, 0]}},
            }
        },
        {"$sort": {"_id": 1}},
    ]

    result = list(collection.aggregate(pipeline))
    return jsonify(result)


# Route for bar chart data
@app.route("/api/shark_attacks", methods=["GET"])
def get_shark_attacks():
    start_year = 2018
    end_year = 2023

    pipeline = [
        {
            "$match": {
                "Date": {
                    "$gte": datetime.strptime("2018-01-01", "%Y-%m-%d"),
                    "$lte": datetime.strptime("2023-12-31", "%Y-%m-%d"),
                }
            }
        },
        {
            "$project": {
                "year": {"$year": "$Date"},
                "month": {"$month": "$Date"},
            }
        },
        {"$group": {"_id": {"year": "$year", "month": "$month"}, "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
    ]

    result = collection.aggregate(pipeline)
    response = [
        {
            "Date": f"{item['_id']['year']}-{item['_id']['month']:02d}",
            "Count": item["count"],
        }
        for item in result
    ]

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
