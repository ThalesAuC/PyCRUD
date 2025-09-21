import os
from pymongo import MongoClient # pyright: ignore[reportMissingImports]

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "SmartFichas"

def get_database():
    client = MongoClient(MONGO_URI)
    return client[DB_NAME]