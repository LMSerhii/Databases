import pymongo
import datetime


from mongo_auth import user, password

uri = f"mongodb+srv://{user}:{password}@cluster0.lmgyayr.mongodb.net/?retryWrites=true&w=majority"

try:
    client = pymongo.MongoClient(uri)
    db = client.testdata
    coll = db.users

    # # add one
    # coll.insert_one(
    # {
    #     '_id': 3,
    #     'user': 'serhii',
    #     'status': True,
    #     'date': datetime.datetime.now().strftime("%m %d %Y %H:%M"),
    #         'parametr': {
    #             'height': {
    #                 'metr': 1,
    #                 'cm': 90,
    #             },
    #             'weight': 150
    #         }
    #     }
    # )

    # # add many
    # data = [
    #     {
    #         '_id': 7,
    #         "name": "pizza",
    #         "type": "thin",
    #         "components": ["pear", "tomato", "peperoni"]
    #     },
    #     {
    #         '_id': 8,
    #         "name": "pizza",
    #         "type": "fat",
    #         "components": ["apple", "crimy", "peperoni"]
    #     },
    # ]
    # coll.insert_many(data)


    # find
    cursor = coll.find(
        {
            "user": 'serhii'
        }
    )
    print(cursor)
    for row in cursor:
        print(row)
    print("-" * 30)

    # show status, date and don`t show _id
    res = coll.find({}, {"_id": 0, "status": 1, "date": 1})
    for value in res:
        print(value)
    print("-" * 30)


    # # show with filter
    query = {"status": "active"}
    res = coll.find(query, {"_id": 0, "status": 1, "user": 1, "date": 1})
    for value in res:
        print(value)
    print("-" * 30)

    # only those users witch name begin on "s"
    query = {"user": {"$gt": "s"}}
    res = coll.find(query, {"status": 1, "user": 1})
    for value in res:
        print(value)
    print("-" * 30)

    # regex
    query = {""}

    print("-" * 30)
    print("Successfully...")
except Exception as ex:
    print("Something wrong..")
    print(ex)
finally:
    client.close()



