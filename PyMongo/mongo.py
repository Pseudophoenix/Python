from pymongo import MongoClient
MONGODB_URI="mongodb+srv://waynerooney0089:00890089ak@cluster0.sazdoor.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(MONGODB_URI)
for db_name in client.list_database_names():
    print(db_name)
