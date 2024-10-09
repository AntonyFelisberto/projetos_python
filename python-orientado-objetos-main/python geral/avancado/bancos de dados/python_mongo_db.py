#mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]

#hostX		Optional. You can specify as many hosts as necessary. You would specify multiple hosts, for example, for connections to replica sets.
#:portX		Optional. The default value is :27017 if not specified.
#database	Optional. The name of the database to authenticate if the connection string includes authentication credentialsIf /database is not specified and the connection string includes credentials, the driver will authenticate to the admin database.
#?options	Connection specific options

import pymongo
from pymongo import MongoClient
from datetime import datetime

uri = "mongodb://localhost:27017/"

client = MongoClient(uri)

db = client['test_db']

collection = db.test_collection
client = pymongo.MongoClient('localhost', 27017)
db = client.mydb.mycollection

for doc in db.find():
   db.update(
       {'_id': doc['_id']}, 
       {'$set': {'newField': 10} }, upsert=False, multi=False)

date_from = datetime(2010, 1, 1)
date_to = datetime(2011, 1, 1)
db.find({ "date": { "$gte": date_from, "$lt": date_to } })

db.find({"frequencies": { "$exists": True }})

print(collection.find_one())

collection.save({"hello":"world"})