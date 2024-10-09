from pymongo import MongoClient
from src.config.config import config


client = MongoClient(config.get("mongo_uri"))
db = client[config.get("database_name")]
