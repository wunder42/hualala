# coding=utf-8
from mongoengine import *
import datetime

class Category(Document):

	name = StringField(required=True, unique=True)
	create_at = DateTimeField(default=datetime.datetime.now)
	change_at = DateTimeField(default=datetime.datetime.now)

class TodoItem(Document):

	content = StringField(required=True)
	# priority = FloatField(required=True)
	category = ReferenceField(Category)
	create_at = DateTimeField(default=datetime.datetime.now)
	change_at = DateTimeField(default=datetime.datetime.now)