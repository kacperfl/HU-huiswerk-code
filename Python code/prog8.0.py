import requests
import json

resource_uri = "https://api.github.com/users/kacperfl"
response = requests.get(resource_uri)
response_data = response.json()

leesbaar = json.dumps(response_data, indent=4)
# print(leesbaar)

resource_uri_ip = "https://ipapi.co/json"
response_ip = requests.get(resource_uri_ip)
response_data_ip = response_ip.json()

ip_adress = json.dumps(response_data_ip["ip"])
stad = json.dumps(response_data_ip["city"])
longitude = json.dumps(response_data_ip["longitude"], indent=2)

print(f"{ip_adress} {stad} {longitude}")