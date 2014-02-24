# coding=utf-8

import json
import tornado.web

from models import Category, TodoItem

class ItemAdd(tornado.web.RequestHandler):

	def post(self):
		''''''
		content = self.get_argument('content')
		category = Category.objects(name=self.get_argument('category')).first()
		print category
		try:
			TodoItem(content=content, category=category).save()
		except Exception, e:
			return self.write(json.dumps({'stat':'error'}))
		return self.write(json.dumps({'stat':'ok'}))

class ItemDelete(tornado.web.RequestHandler):

	def get(self, tid):
		''''''
		try:
			print tid
			TodoItem.objects(id=tid).delete()
		except Exception, e:
			return self.write(json.dumps({'stat':'error'}))
		return self.write(json.dumps({'stat':'ok'}))

class ItemUpdate(tornado.web.RequestHandler):

	def post(self, tid):
		''''''
		content = self.get_argument('content')
		try:
			print tid, content
			TodoItem.objects(id=tid).update_one(set__content=content)
		except Exception, e:
			return self.write(json.dumps({'stat':'error'}))
		return self.write(json.dumps({'stat':'ok'}))
