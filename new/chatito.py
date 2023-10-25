import pandas as pd
import json
import urllib.parse
import requests as rq
import base64

# Juan's Keys
# Apikey: 6wiyhy9vfz8e4u0m8e56legl0jr21mvf
# Secret: QK5HdSIKI20n

# Franco's Keys
# Apikey: 2zky9zdsmvowg05bx61lsmyvxthkewum
# Secret: HtvQmb7FUAzj


# Gets the bearer_token
def get_oauth_token():
    url = "https://api.idealista.com/oauth/token"

    apikey= '6wiyhy9vfz8e4u0m8e56legl0jr21mvf'
    secret= 'QK5HdSIKI20n'

    auth = base64.b64encode((apikey + ':' + secret).encode('utf-8'))
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Authorization' : 'Basic ' + auth.decode('utf-8')}
    params = urllib.parse.urlencode({'grant_type':'client_credentials'})

    content = rq.post(url,headers = headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    return bearer_token



# Searches idealista with our inputs
def search_api(token, url):
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization': 'Bearer ' + token}
    content = rq.post(url, headers=headers)
    response = json.loads(content.text)
    if 'result' in response:
        return response['result']
    else:
        return []



# Our inputs / filters
inputs = {
    'country': 'es', #values: es, it, pt
    'locale': 'es', #values: es, it, pt, en, ca
    'language': 'es',
    'max_items': '50',
    'operation': 'sale',
    'property_type': 'homes',
    'order': 'priceDown',
    'center': '40.4167,-3.70325', # Sol Coordinates
    'distance': '60000', # Distance to center in meters
    'sort': 'desc',
    'bankOffer': 'false',
}


# Initialize empty dataframe to fill and limit of searches
df_tot = pd.DataFrame()
limit = 2

# Iterating over the limit of searches with the inputs
# Each iteration of a search inserts a record into the df
for i in range(1, limit + 1):
    url = (
        'https://api.idealista.com/3.5/' + inputs['country'] + '/search?operation=' + inputs['operation'] +
        '&maxItems=' + inputs['max_items'] +
        '&order=' + inputs['order'] +
        '&center=' + inputs['center'] +
        '&distance=' + inputs['distance'] +
        '&propertyType=' + inputs['property_type'] +
        '&sort=' + inputs['sort'] +
        '&numPage=%s' % i +
        '&language=' + inputs['language']
    )

    search_results = search_api(get_oauth_token(), url)
    if not search_results:
        print("No results")
        break
    print(f"Successful search {i}")

    df = pd.DataFrame.from_dict(search_results['elementList'])
    df_tot = pd.concat([df_tot, df])

df_tot = df_tot.reset_index()
df_tot.to_csv('df.csv')
