# -*- coding : utf-8 -*-

from mongoengine import *

class User(Document):
    email = StringField(required=True)
    password =StringField(min_length=6)
    name = StringField(max_length=50)
    avatar = URLField()
