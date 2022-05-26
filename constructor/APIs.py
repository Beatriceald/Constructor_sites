import requests
import json

url = "https://api.freepik.com/v1/resources?locale=en-GB&page=1&limit=2&order=latest&term=car"

payload={}
headers = {
  'Accept-Language': 'en-GB',
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Freepik-API-Key': '00000000-0000-0000-0000-000000000000'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)