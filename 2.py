import requests

def shakespeare(prompt:str):
	try:
		url = "https://shakespeare.p.rapidapi.com/shakespeare.json"

		querystring = {"text":prompt}

		headers = {
			"X-FunTranslations-Api-Secret": "<REQUIRED>",
			"X-RapidAPI-Key": "8e509378a7msh7ec80bafb25d574p1643dajsn93e5b378c05f",
			"X-RapidAPI-Host": "shakespeare.p.rapidapi.com"
		}

		response = requests.get(url, headers=headers, params=querystring)

		print(response.json()['contents']['translated'])
	except Exception as e:
		print(e)

shakespeare('These nuts are on your chin')