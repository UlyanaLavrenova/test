from flask import Flask
import jsonpickle
import json
from flask_cors import CORS

# try:
#     with open("WireFrame1.txt") as info:
#         client_info = json.load(info)
#         lines = ''
#         y = 1
#         for x in client_info['clientGbg']:
#             lines += ('{id: '+str(y)+', itemName: \''+x[0].replace('\'','')+' | '+x[1].replace('\'','')+'\'},')
#             y += 1
#         print(lines)
#         # with open('../cloudhalo/vendors.txt', 'w') as client:
#             # client.write(json.dumps(lines))
#
# except FileNotFoundError:
#     client_info = "File not found"

try:
    with open("WireFrame1.txt") as info:
        client_info = json.load(info)
        lines = ''
        y = 1
        for x in client_info['market']:
            lines += ('{id: ' + str(y) + ', itemName: \'' + x +'\'},')
            y += 1
        print(lines)
        # with open('../cloudhalo/vendors.txt', 'w') as client:
            # client.write(json.dumps(lines))

except FileNotFoundError:
    client_info = "File not found"