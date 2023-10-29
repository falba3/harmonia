import pandas as pd
import json
import urllib.parse as urllib
import requests as rq
import base64

# Juan's Keys
# Apikey: 6wiyhy9vfz8e4u0m8e56legl0jr21mvf
# Secret: QK5HdSIKI20n

# Franco's Keys
# Apikey: 2zky9zdsmvowg05bx61lsmyvxthkewum
# Secret: HtvQmb7FUAzj

def get_oauth_token():
    url = "https://api.idealista.com/oauth/token"
    apikey = '6wiyhy9vfz8e4u0m8e56legl0jr21mvf'
    secret = 'QK5HdSIKI20n'
    auth_str = f"{apikey}:{secret}"
    auth_bytes = auth_str.encode('utf-8')  # Encode the string to bytes
    auth = base64.b64encode(auth_bytes).decode('utf-8')  # Encode to base64 and decode to a string
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Authorization': 'Basic ' + auth}
    params = urllib.urlencode({'grant_type': 'client_credentials'})
    content = rq.post(url, headers=headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    # with open('bearer_token', 'w') as file:
    #      json.dump(bearer_token, file, indent=4)
    return bearer_token


def search_api(token, url):
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
    content = rq.post(url, headers = headers)
    result = json.loads(content.text)
    return result['elementList']

country = 'es' #values: es, it, pt
locale = 'es' #values: es, it, pt, en, ca
language = 'es'
max_items = '25'
operation = 'sale'
property_type = 'homes'
order = 'priceDown'
center = '40.4167,-3.70325'
distance = '60000'
sort = 'desc'
bankOffer = 'false'

df_tot = pd.DataFrame()
limit = 78 # 78 + 12 = 90 * 25 = 2250

for i in range(1,limit):
    try:
        url = ('https://api.idealista.com/3.5/'+country+'/search?operation='+operation+#"&locale="+locale+
               '&maxItems='+max_items+
               '&order='+order+
               '&center='+center+
               '&distance='+distance+
               '&propertyType='+property_type+
               '&sort='+sort+
               '&numPage=%s'+
               '&language='+language) %(i)
        res = search_api(get_oauth_token(), url)
        if not res:
            print("No results")
            df_tot = df_tot.reset_index()
            df_tot.to_csv('df_3.csv')
            break
        print(f"Successful search {i}")
        df = pd.DataFrame(res)
        df_tot = pd.concat([df_tot,df])
    except Exception as e:
        df_tot.to_csv('df_3.csv')
        print(e)
        break



df_tot = df_tot.reset_index()
df_tot.to_csv('df_3.csv')