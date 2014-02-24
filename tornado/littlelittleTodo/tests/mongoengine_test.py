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
	catetory = ReferenceField(Category)
	create_at = DateTimeField(default=datetime.datetime.now)
	change_at = DateTimeField(default=datetime.datetime.now)


def test():

	connect('littlelittleTodo')
	# a = Category(name='plan').save()
	print Category.objects(name='plan').first()

	# TodoItem(content='today, tornado', catetory=a).save()

	# Category.objects(name='plan').update_one(set__change_at=datetime.datetime.now)
	# Category.objects(name='plan').delete()



if __name__ == '__main__':

	test()