import sys
path='C:/wamp/www/abydeen/rapidwsgi/src/'
sys.path.append(path)
import threading
import setting
import base
from base import exception
from base import io
import app

def application(environ, start_response):
   
	#data=base.request.get(environ)
	webinfo = threading.local()
	webinfo.request = base.io.Request(environ)
	webinfo.response = base.io.Response(start_response)
	dispatcher=base.io.Dispatcher()
	
	if not dispatcher.exist_path(environ):
		mod="app" + "." + setting.default_controller
		path = getattr(sys, "path")
		#raise TypeError(path)
		__import__(mod)
		reference = getattr(app, setting.default_controller)
		reference.default(webinfo.request, webinfo.response)
	else:
	    reference = dispatcher.find_object(app, environ)
	    if callable(reference):
	        reference(webinfo.request, webinfo.response)
	    else:
	        if callable(reference.default):
	            reference.default(webinfo.request, webinfo.response)
	
	return webinfo.response.push()
application = base.exception.ExceptionMiddleware(application)


