from pymongo import MongoClient # pyright: ignore[reportMissingImports]

def get_database(db_name="SmartFichas"):
    client = MongoClient("mongodb://localhost:27017/")
    return client[db_name]
