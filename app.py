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
    client = MongoClient('mongodb://localhost:27017/')
    return client

def get_sharks_collection():
    client = get_mongo_connection()
    db = client.sharks_db
    collection = db.attacks
    return collection

# Route to serve the html file
@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

# Route to get all data
@app.route("/", methods=['GET'])
def get_all_data():
    collection = get_sharks_collection()
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

# Route to get shark attack data based on year and fatal filters
@app.route("/shark_attacks", methods=['GET'])
def get_shark_attacks():
    # Get the query parameters from the request
    year = request.args.get('year')
    fatal = request.args.get('fatal')

    # Fetch data from Mongo database and filter based on year and fatal
    collection = get_sharks_collection()
    query = {}
    if year and year != "All":
        query['Year'] = int(year)
    if fatal and fatal != "All":
        query['Fatal (Y/N)'] = fatal
    data = list(collection.find(query, {'_id': 0}))

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
