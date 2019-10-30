import json

with open ('subway_info.json') as js:
    data = json.load(js)
    print(data)