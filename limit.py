import requests

url = "https://scrapers-proxy2.p.rapidapi.com/standard"

querystring = {"url":"https://pitchbook.com/profiles/company/51261-67"}

headers = {
    'x-rapidapi-host': "scrapers-proxy2.p.rapidapi.com",
    'x-rapidapi-key': "4813778e31msh5fd509d01a125bfp15fa1djsn42e008553dce"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
