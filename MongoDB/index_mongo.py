import pymongo
from itertools import count
import datetime

from mongo_auth import user, password

client = pymongo.MongoClient(
    f"mongodb+srv://{user}:{password}@cluster0.fwfate3.mongodb.net/?retryWrites=true&w=majority"
)

db = client.testdata
coll = db.users

for i in count(0, 1):
    data = {

        "_id": i,
        "login": f"name_{i}",
        "password": f"passw{i}",
        "time": datetime.datetime.now()
    }
    coll.insert_one(data)
    print(f"{i}: Данні записані")



