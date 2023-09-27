key = '8e509378a7msh7ec80bafb25d574p1643dajsn93e5b378c05f'
host = 'idealista2.p.rapidapi.com'

import requests
import json

url = "https://idealista2.p.rapidapi.com/auto-complete"

querystring = {"prefix":"madrid","country":"es"}

headers = {
	"X-RapidAPI-Key": "8e509378a7msh7ec80bafb25d574p1643dajsn93e5b378c05f",
	"X-RapidAPI-Host": "idealista2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_json = response.json()

with open('response.json', 'w') as json_file:
    json.dump(response_json, json_file, indent=4)