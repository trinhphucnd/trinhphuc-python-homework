from mongoengine import *


class Customers(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contact = BooleanField()
