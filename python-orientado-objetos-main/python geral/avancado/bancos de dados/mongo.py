#python -m pip install pymongo
import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = db["sample"]     #create db
mycln = mydb["details"] #create collection

mydict = { "name": "foo", "age": 20 }
#insert a single document
doc = mycln.insert_one(mydict)
# insert multiple documents
mylist =[
    {"name": "foo", "age": 20},
    {"name": "bar", "age": 25},
    {"name": "apple", "age": 30}
]
doc1 = mycln.insert_many(mylist)

# to update a single document
mycln.update_one({"name" : "foo"}, {"$set":{"age": 23}})
doc1 = mycln.find({"name" : "foo"})
print(doc1)

# to delete a single document
doc1 = mycln.delete_one({"name" : "foo"})
print(doc1)

# Mongodb by default creates an id for each document
print(doc1.inserted_ids)
#to return all the documents
for doc in mycln.find():
  print(doc)
# to return first occurence
doc1=mycln.find_one()
print(doc1)
#to return list of names whose age is greater than 20
qry = { "age": { "$gt": 30 } }
for doc3 in mycln.find(qry):
    print(doc3)