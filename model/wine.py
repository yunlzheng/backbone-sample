# -*- coding : utf-8 -*-

from mongoengine import *

class Wine(Document):
    name = StringField()
    grapes =StringField()
    country = StringField()
    region = StringField()
    year = StringField()
    notes = StringField()
