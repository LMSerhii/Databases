import pymongo

from mongo_auth import user, password

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority"
)
db = client.testdata
users = db.users
coll = users

res = coll.count_documents({})
print(res)

res = coll.count_documents({"user": "Serhii"})
print(res)

res = coll.count_documents({"user": {"$regex": "S"}})
print(res)

res = client.list_database_names()
print(res)

res = db.list_collection_names()
print(res)

coll.drop()
print("collection was drop")
