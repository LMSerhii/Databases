import pymongo

from mongo_auth import user, password

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority")
db = client.testdata
coll = db.users

res = coll.find({}, {"_id": 0, "status": 1, "date": 1})
for value in res:
    print(value)

print("-" * 30)

query = {"status": False}

res = coll.find(query, {"_id": 0, "status": 1, "date": 1})
for value in res:
    print(value)

print("-" * 30)

query = {"status": True}
for value in coll.find(query, {"_id": 0, "status": 1, "user": 1}):
    print(value)

print("-" * 30)

# # возвращает то что начинается на букву и ниже по алфавиту
query = {"user": {"$gt": "S"}}
for value in coll.find(query, {"_id": 0, "status": 1, "user": 1}):
    print(value)

print("-" * 30)

query = {"user": {"$regex": "Sv"}}
for value in coll.find(query):
    print(value)

print("-" * 30)

print(coll.find_one({"user": {"$regex": "Ser"}}))
print("-" * 30)

for value in coll.find().limit(2):
    print(value)

print("-" * 30)

for value in coll.find().sort("_id", -1):
    print(value)

print("-" * 30)