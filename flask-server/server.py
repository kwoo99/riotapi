from flask import Flask

import json

app = Flask(__name__)


@app.route("/profiles")
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
    
    return rex


if '__name__' == "__main__":
    app.run(host='0.0.0.0', port=5000)
