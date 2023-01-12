import pymongo

from mongo_auth import user, password

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority"
)
db = client.testdata
coll = db.users

for i in range(20):
    coll.insert_one(
        {
            "_id": i,
            "name": f"test_{i}"
        }
    )

# current = {"name": "test_3"}
# new_data = {"$set": {"name": "new"}}
#
# coll.update_one(current, new_data)


# current = {"name": {"$regex": "test."}}
# new_data = {"$set": {"name": "new"}}
#
# coll.update_many(current, new_data)

# current = {"_id": 1}
# new_data = {"$inc": {"balance": +300}}
# coll.update_one(current, new_data)

# удаление по индексу
# current = {"_id": 1}
# new_data = {"$pop": {"arrage": 1}}
# coll.update_one(current, new_data)

# удаление по значению
# current = {"_id": 1}
# new_data = {"$pull": {"arrage": "hello"}}
# coll.update_one(current, new_data)
