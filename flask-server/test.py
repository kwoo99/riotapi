import json
import sys

d = open('/Users/kylewoo/Documents/GitHub/riotapi/riotapi/profiles.json')
data = json.load(d)
print(data)