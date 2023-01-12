import pymongo

from mongo_auth import user, password

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority"
)
db = client.testdata
coll = db.users
