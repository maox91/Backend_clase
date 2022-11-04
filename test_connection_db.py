import pymongo
import certifi

ca= certifi.where()


client = pymongo.MongoClient(
    "mongodb+srv://maox91:000Cerdo@mintic4.dcsgdl0.mongodb.net/academic_db?retryWrites=true&w=majority",
    tlsCAFile=ca
                             )
db = client.test
print(db)

data_base = client["academic_db"]
print(data_base.list_collection_names())

student_collection = data_base.get_collection("student")
all_students = student_collection.find({})
print(all_students)