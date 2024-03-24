from pymongo import MongoClient
MONGODB_URI="mongodb://localhost:27017"

client=MongoClient(MONGODB_URI)
for db_name in client.list_database_names():
    print(db_name)
