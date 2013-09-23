# coding: utf-8
import json
import os.path
import functools

import tornado.ioloop
import tornado.web
from tornado.util import import_object
from tornado.log import app_log
from mongoengine import connect

ROOT_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(ROOT_DIR, "static")
TEMPLATE_DIR = os.path.join(ROOT_DIR, "templates")

def load_model(func):
    """注入一个Model参数给函数."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        #setattr(self, 'session', "session")
        print "revice args {0} kwargs {1}".format(args, kwargs)
        model_class = "model.{0}".format(args[0])
        try:
            model = import_object(model_class)
            print "import object {0}".format(model)
            setattr(self, 'model', model)
        except Exception as ex:
            app_log.error(ex)
            print ex
            raise tornado.web.HTTPError(404)
        print 'revice request args: {0} kwargs: {1}'.format(args, kwargs)
        return func(self, *args, **kwargs)
    return wrapper

class BackboneHandler(tornado.web.RequestHandler):

	'''
	HTTP GET
		url_root/{model}/{uuid}
		url_root/{model}
	HTTP POST
		url_root/{mode}  data=model
	HTTP DELETE
		url_root/{mode}/{uuid}
	HTTP POST
		url_root/{mode}/{uuid} data=update_model
	'''
	def initialize(self, auth= False):
		self.auth = auth

	def prepare(self):
		if self.auth:
			if not self.current_user:
				raise tornado.web.HTTPError(403)

	def encode(self, data):
		return json.dumps(data)

	def decode(self, data):
		return json.loads(data)

	def get(self, *args):
		if self.is_get_collection(*args):
			self.write(self.encode(self.get_collection(*args)))
		else:
			self.write(self.encode(self.get_model(*args)))

	def post(self, *args):
		resp = self.encode(self.create_model(*args))
		self.write(resp)

	def put(self, *args):
		resp = self.encode(self.update_model(*args))
		self.write(resp)

	def delete(self, *args):
		self.delete_model(*args)

	def is_get_collection(self, *args):
		return len(args) == 1

	def create_model(self, obj, *args):
		raise tornado.web.HTTPError(404)

	def get_collection(self, *args):
		raise tornado.web.HTTPError(404)

	def get_model(self, *args):
		raise tornado.web.HTTPError(404)

	def update_model(self, obj, *args):
		raise tornado.web.HTTPError(404)

	def delete_model(self, *args):
		raise tornado.web.HTTPError(404)

class MongoBackboneHandler(BackboneHandler):

	def encode(self,data):
		resp = {}
		if isinstance(data, self.model):
			resp = data.to_json()
		else:
			resp = [obj.to_json() for obj in data]
			resp = json.dumps(resp)
		return resp

	@load_model
	def get_model(self, *args):
		try:
			instance = self.model.objects(id=args[1])[0]
		except Exception as ex:
			app_log.error(ex)
			raise tornado.web.HTTPError(404)
		else:
			return instance

	@load_model
	def get_collection(self, *args):
		return self.model.objects()

	@load_model
	def delete_model(self, *args):
		try:
			instance = self.model.objects(id=args[1])[0]
			instance.delete()
		except Exception, e:
			raise e
		else:
			return instance

	@load_model
	def create_model(self, *args):
		#print obj
		obj = self.decode(self.request.body)
		obj = self.model(**obj)
		obj.save()
		return obj

	@load_model
	def update_model(self, *args):
		obj = self.decode(self.request.body)
		instance = self.model.objects(id=args[1])[0]
		for key in obj:
			print key
			if hasattr(instance, key):
				setattr(instance, key, obj[key])
		instance.save()
		return instance

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("what-is-view.html");

settings = dict(
    template_path=TEMPLATE_DIR,
    static_path= STATIC_DIR,
    login_url="/sigin",
    debug=True
)

connect('test', host="mongodb://localhost:27017")

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/api/([a-z]+)", MongoBackboneHandler),
    (r"/api/([a-z]+)/(.+)", MongoBackboneHandler),
], **settings)

if __name__ == '__main__':
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()