import json

# with open('response.json', 'r') as json_file:
data = json.load(open('response.json', 'r'))
data = data['locations']

for i in data:
    print(f"{i['name']}: {i['subTypeText']}")
