from pymongo import MongoClient
import os
from src.config.config import config


mongo_uri = os.getenv("MONGO_URL", config.get("mongo_uri"))
database_name = config.get("database_name")

client = MongoClient(mongo_uri)
db = client[database_name]