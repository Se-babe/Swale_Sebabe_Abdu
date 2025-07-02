# Basics get request using the library requests
import requests 

response = requests.get("https://api.github.com")
# Check if the request was successful
print("Status Code:", response.status_code)  # Should print 200 for success
print("Response.json:", response.json())  # Print response JSON 
