from flask import Flask, request, jsonify, render_template

from flask_cors import cross_origin, CORS

import logging

import json 

# logging.getLogger('flask_cors').level = logging.DEBUG

# Flask.logger_name = "listlogger"
app = Flask(__name__)
# CORS(app, resources={r"/add": {"origins": "http://localhost:5000"}})
# cors = CORS(app, resources={r'*': {'origins': '*'}})
CORS(app, support_credentials=True)
# app.config['CORS_HEADERS'] = 'Content-Type'


# @app.after_request
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
#     response.headers['Access-Control-Allow-Methods'] = 'POST'
#     return response

# @app.route("/")
# def index():
#     return render_template("http://localhost:5000/")

@app.route("/profiles", methods = ["GET"])
@cross_origin(supports_credentials=True)
def teams():
    d = open('../riotapi/profiles.json')
    data = json.load(d)
    rex = {
        "y": {
        "a": "h",
        "b": "g",
        "c": "r",
        "d": "e"
    },
        "j": {
        "a": "h",
        "b": "g",
        "c": "r",
        "d": "e"
    },
        "k": {
        "a": "h",
        "b": "g",
        "c": "r",
        "d": "e"
    }
    }
    
    return jsonify(rex)

@app.route("/add", methods=["POST", "GET"])
@cross_origin(supports_credentials=True)
def receive_data():
    data = request
    if request.method == "POST":
        data = request.form["name"]
        print(data)
    print('hello world')
    # data = request.form["age"]
    response = {'message': 'Data received successfully'}
    return jsonify(response)


if '__name__' == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)