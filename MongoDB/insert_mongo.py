import pymongo
import datetime

from mongo_auth import user, password

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority")
db = client.testdata
coll = db.users

coll.insert_one(
    {
        "_id": 1,
        "user": "Serhii",
        "status": True,
        "date": datetime.datetime.now().strftime("%m %d %Y %H:%M")
    }
)

data = [
    {
        "_id": 2,
        "user": "Jack",
        "status": True,
        "date": datetime.datetime.now().strftime("%m %d %Y %H:%M")
    },
    {
        "_id": 3,
        "user": "Svetlana",
        "status": False,
        "date": datetime.datetime.now().strftime("%m %d %Y %H:%M")
    }

]

coll.insert_many(data)
