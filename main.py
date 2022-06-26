import requests
import json


api_key = input("ENTER YOUR API KEY HERE:")
user = input("What user would you like to search for? ")

r = requests.get("https://fortnite-api.com/v2/stats/br/v2")
data = r.json()
with open(f'stats.json', 'w') as f: 
  json.dump(data, f, indent=3)
print("Data Has Been Dumped Into File Directory stats.json")
