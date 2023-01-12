import pymongo

from mongo_auth import user, password

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority"
)
db = client.testdata
coll = db.users

# coll.delete_one({"_id": 0})

# query = {"name222": {"$regex": "new2"}}
# coll.delete_many(query)

# query = {"name": {"$regex": "new"}}
# res = coll.delete_many(query)
# print(f"deleted: {res.deleted_count}")

res = coll.delete_many({})
print(f"deleted: {res.deleted_count}")
