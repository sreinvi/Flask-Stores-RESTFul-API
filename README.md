# Flask-Stores-RESTFul-API
Simple implementation of a RESTFul API where you can register stores to a database and create items that contain a name and a price associated to that store. You are able to also register to the database and, for some endpoints, you need to authenticate using JWT.

# First Thing First

You should have `Python version >= 3.6` installed on your machine. With it, you can use the `pip` package manager to install all the dependecies required to get the API running as follows:

> pip install -r requirements.txt

Once you do, you are able to initiate the web server.

# Initiate the Web Server

For you to initiate the webserver, all you need to do is:

> python app.py

in the root folder. This will set up the webserver in your localhost 5000. You can test it going to http://localhost:5000/items and verify that you got an empty json back in your webpage.

# Consume the API

For you to consume the API, i recommend using [Postman](https://www.postman.com/). There are 6 endpoints:

1. /items (GET)
2. /item/<name> (GET, POST, PUT, DEL)
3. /auth (POST)
4. /register (POST)
5. /store/<name> (POST0)
6. /stores (GET)

Since it's a RESTFul API, it communicates through JSON. Use postman to implement all the endpoints above and remember to add `Content-Type: application/json` to the HTTP Header.

Here is some examples of JSON for each endpoing you can send:

1. For the authentication part:
- POST /register: {"username": "CHRISTIAN", "password": "ThatsNoice"}
- POST /auth: {"username": "CHRISTIAN", "password": "ThatsNoice"} # You shall receive the JWT here as return

Some endpoints methods require your authentication. You can do it by adding `Authorization: JWT your_token` to the HTTP Header.

2. For the /store endpoint:
- POST /store/1 

Here you have created an store with store_id equals 1.

4. For the /stores endpoint:
- GET /stores

This shall return you all the stores and the items within each one.

5. For the /item endpoint:
- POST /item/Chair: {"price": 150.99, "store_id": 1} # Create new item
- GET /item/Chair # GET the item by its name
- PUT /item/Chair: {"price": 165.99, "store_id": 1} # Create or alter an item
- DEL /item/Chair # Delete an item
