import requests
import json

response = requests.get("https://api.github.com")
print(json.dumps(response.json(), indent=2))
