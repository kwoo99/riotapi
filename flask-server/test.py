import json
import sys

d = open('../riotapi/profiles.json')

data = json.load(d)
print(data)