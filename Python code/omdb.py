import requests
import json

url = "http://www.omdbapi.com/?i=tt3896198&apikey=d5c0bcad&t=Rocky"
response = requests.get(url)
data = response.json()

leesbaar = json.dumps(data, indent=2)

title = data["Title"]
id = data["imdbID"]

print(f"{title} {id}")