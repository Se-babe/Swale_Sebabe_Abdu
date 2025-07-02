#creating a new data using the POST method

#Basics of POST request using the requests library
import requests

#example API endpoint
url = "https://jsonplaceholder.typicode.com/posts"
#data to be sent in the POST request    
data = {
    "title": "sebabe",
    "body": "abdul",
    "userId": 1
    
}   
#sending the POST request
response = requests.post(url, json=data)

#print the status code and json response
print("Status Code:", response.status_code)  # Should print 201 for created
print("Response.json:", response.json())  # Print response JSON
