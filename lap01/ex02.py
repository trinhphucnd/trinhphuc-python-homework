from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']
new_post = {
    "title" :  "Bánh Trà",
    "author" : "Trịnh Phúc",
    "content": "Thanh xuân như miếng bánh trà. Ăn xong miếng bánh hết bà thanh xuân"
    } 

posts.insert_one(new_post)