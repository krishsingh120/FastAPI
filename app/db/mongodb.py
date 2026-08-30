from app.core.config import settings
from pymongo import MongoClient

mongo_uri = settings.mongo_url
db_name = settings.database_name



# connect to mongodb server
client = MongoClient(mongo_uri)


# create a db with db name from .env
db = client[db_name]

# create collections
users_collection = db["users"]