import pymongo

client = pymongo.MongoClient(
    'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.1'
)
db = client.testdata
coll = db.users
coll.insert_one(
    {
        "_id": 4,
        "User": "Roman"
    }
)
coll.insert_one(
    {
        "_id": 5,
        "User": "Svetlana"
    }
)

res = coll.find_one()
print(res)

res = coll.find()
for value in res:
    print(value)