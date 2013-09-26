# -*- coding : utf-8 -*-

from mongoengine import *

class Todo(Document):
    title = StringField(required=True, default="")
    completed =BooleanField(required=True, default=False)
