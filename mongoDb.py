import pymongo

#join to servis
myclient =  pymongo.MongoClient('mongodb://localhost:27017/')

#create a database
mydb = myclient['mydatabase']

for name in myclient.list_database_names():
    print(name)

#create a table
mycol = mydb['customers']

#create a record
mydict = {'name' : 'John', 'address' : 'Highway 37'}

"""
#and add it to the database
x = mycol.insert_one(mydict)

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

#we can also insert a list of records
x = mycol.insert_many(mylist)
"""
#but what about searching
x = mycol.find_one()

#print(x)

#find all
#for rec in mycol.find():
#    print(rec)

#ommit id field
#for rec in mycol.find({},{'_id':0, 'name':1, 'address':1}):
#    print(rec)    

#query
#myquery = {'address' : 'Green Grass 1'}
#for rec in mycol.find(myquery):
#    print(rec)

#sorting
myquery = {'address' : {'$gt' : 'S'}}
for rec in mycol.find(myquery).sort('name'): #or descending sort('name', -1)
    print(rec)

#myquery = {'address' : {'$regex' : '^S'}}
#for rec in mycol.find(myquery):
#    print(rec)        