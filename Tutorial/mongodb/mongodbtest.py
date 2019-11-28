from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://admin:test@testdb-igmv7.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.marcom
marcomdata = db.marcom_col.find_one({'name': "MarCOM"})
pprint(marcomdata['name'])

#CreateToCollection
test_data={
    'unique_data': 12312321123123,
    'new_name': "MARCOMNEWTEST"
}
result=db.marcom_col.insert_one(test_data)

marcomresult = db.marcom_col.find_one({'new_name': "MARCOMNEW"})
pprint(marcomresult['unique_data'])
