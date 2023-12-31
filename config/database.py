import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

uri = os.getenv("MONGO_CONNECTION_STRING")

client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]
