from mongoengine import *

# Create collection
# design database

class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() # 0 = female , 1 = male
    phone = StringField()
    address = StringField()
    status = BooleanField()