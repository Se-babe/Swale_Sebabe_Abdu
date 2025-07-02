# introduction
#API'S (appilcation programming interface) are used to connect different software applications and allow them to communicate with each other. In this case, the Telegram API is used to connect the bot to the Telegram platform, allowing it to send and receive messages, manage channels, and perform other actions.
#The API provides a set of methods and endpoints that the bot can use to interact with Telegram's features, such as sending messages, creating polls, and managing user interactions.

#types of API's
#There are several types of APIs, including RESTful APIs, SOAP APIs, and GraphQL APIs.
#1.web APIs: These are APIs that are accessed over the internet using HTTP or HTTPS protocols. They allow applications to communicate with each other over the web.
#2.library APIs: These are APIs that are provided by programming libraries or frameworks. They allow
#3.operating system APIs: These are APIs that are provided by the operating system. They allow applications to interact with the underlying hardware and software of the system.

#understanding RESTFUL APIs
#RESTful APIs are a type of web API that follows the principles of Representational State Transfer (REST). They use standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources, which are typically represented in JSON or XML format. RESTful APIs are stateless, meaning each request from the client contains all the information needed to process it, and they can be easily scaled and cached.
# RESTFUL MEANS RPRESENTATIONAL STATE TRANSFER

# Key rest principles
# 1. Stateless: Each request from the client to the server must contain all the information needed to understand and process the request.
# 2. Client-Server Architecture: The client and server are separate entities that communicate over
#3. Uniform Interface: RESTful APIs should have a consistent and uniform interface, making it easy for clients to interact with the server.
# 4. Resource-Based: RESTful APIs are centered around resources, which are identified by
#5. Cacheable: Responses from the server should be cacheable to improve performance and reduce server load.
#6. Layered System: RESTful APIs can be composed of multiple layers, allowing for scalability and separation of concerns.
# 7. Code on Demand (optional): Servers can provide executable code to clients, allowing them to extend their functionality.

#GET means retrieve data from a server
##POST means send data to a server to create or update a resource
#put means update a resource on a server
#delete means remove a resource from a server

#RESTFUL API endpoints
#POST/API/USERS - Create a new user
#GET/API/USERS - Retrieve a list of users
#GET/API/USERS/{id} - Retrieve a specific user by ID
#PUT/API/USERS/{id} - Update a specific user by ID
#DELETE/API/USERS/{id} - Delete a specific user by ID
#PUT method to update data in the API


#consuming API's with python
#python provides several libraries to consume APIs, such as `requests`, `http.client`, and `urllib`. The most commonly used library is `requests`, which simplifies the process of making HTTP requests and handling responses.

#first you need to install the requests library if you haven't already:
# pip install requests
#live demo using the requests library to consume a RESTful API
import requests

#example API endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts")
#check if the request was successful
print("Status Code:", response.status_code)  # Should print 200 for success
print("Response.json:", response.json())  # Print response JSON

#post method to send data to the API

