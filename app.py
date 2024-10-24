from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


# Connect to MongoDB
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)  
db = client["bookstore_db"]  
collection = db["bookstore_db"]  

from routes import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

    
