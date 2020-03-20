from flask import Flask
import jsonpickle
import json
from flask_cors import CORS

try:
    with open("WireFrame8.txt") as info:
        client_info = json.load(info)
        lines = []
        for x in client_info['vendors']:
            lines.append(x)
        with open('../cloudhalo/vendors.txt', 'w') as client:
            client.write(json.dumps(lines))

except FileNotFoundError:
    client_info = "File not found"
