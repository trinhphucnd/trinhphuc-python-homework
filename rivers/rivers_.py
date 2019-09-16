from mongoengine import *


class River(Document):
    name = StringField()
    length = IntField()
    continent = StringField()
    