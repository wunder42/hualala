# coding=utf-8

import os
from mongoengine import connect

import tornado.web
import tornado.ioloop 
from tornado.options import options, define

from handlers import ItemAdd, ItemDelete, ItemUpdate

define('port', default=9898, type=int)
define("mongo_host", default="127.0.0.1:27017", help="database host")
define("mongo_database", default="littlelittleTodo", help="database name")

class Ak(tornado.web.RequestHandler):

	def get(self):
		self.write('ok')

class Application(tornado.web.Application):

	def __init__(self):

		handlers = [
			(r'/', Ak),
			(r'/t/add', ItemAdd),
			(r'/t/delete/(?P<tid>[^/$]+)', ItemDelete),
			(r'/t/update/(?P<tid>[^/$]+)', ItemUpdate), 
		]

		settings = {
			# 'xsrf_cookies': True,
			'cookie_secret': '64bab51c-9977-11e3-a23f-002655f43ded',
			'login_url': '/login',
			'template_url': os.path.join(os.path.dirname(__file__), 'templates'),
			'static_url': os.path.join(os.path.dirname(__file__), 'static'),
			'debug': True
		}

		super(Application, self).__init__(handlers, **settings)
		connect(options.mongo_database)



if __name__ == '__main__':

	app = Application()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
