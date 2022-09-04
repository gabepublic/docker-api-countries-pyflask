import os
from flask import Flask, jsonify, request, render_template
import json


app = Flask(__name__)
ENVIRONMENT_DEBUG = os.environ.get("DEBUG", False)
PORT = os.environ.get("PORT", 5000)

countries = {}

def load_data():
    print("loading country data...")
    f = open('countries.json')
    data = json.load(f)
    global countries
    countries = data["countries"]
    #print(data)
    #print(countries)
    
@app.route('/')
def index():
    resp = {}
    resp["msg"] = "URIs: /countries /debug /error"
    resp["status"] = "success"
    return jsonify(resp)

@app.route('/debug')
def debug():
    resp = {}
    msg = "URIs: /countries /debug /error"
    resp["msg"] = msg
    resp["status"] = "success"
    return jsonify(resp)

@app.route('/error')
def test_error():
    resp = {}
    msg = "Simulate error"
    resp["msg"] = msg
    resp["status"] = "failure"
    return jsonify(resp)

@app.route('/countries')
def get_countries():
    global countries
    print(countries)
    resp = {}
    resp["msg"] = "Found 5 countries"
    resp["countries"] = countries
    resp["status"] = "success"
    return jsonify(resp)


if __name__ == "__main__":

    load_data()
    print("API Port: ", PORT)
    app.run(host='0.0.0.0', port=PORT, debug=ENVIRONMENT_DEBUG)