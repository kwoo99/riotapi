from flask import Flask

import json

app = Flask(__name__)

@app.route("/")
def teams():
    # d = open('/Users/kylewoo/Documents/GitHub/riotapi/riotapi/profiles.json')
    # data = json.load(d)
    return 'hello'

if '__name__' == "__main__":
    app.run(host = '0.0.0.0', port = 5000) 
    d = open('/Users/kylewoo/Documents/GitHub/riotapi/riotapi/profiles.json')
    data_ = json.load(d)