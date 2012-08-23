import sys
import threading
sys.path.append('C:/wamp/www/abydeen/rapidwsgi/src/')
import app
import base
from app import *
from base import *
import setting

def application(environ, start_response):
   
    #data=base.request.get(environ)
    webinfo = threading.local()
    webinfo.request = base.io.Request(environ)
    webinfo.response = base.io.Response(start_response)
    #output=str(webinfo.request.http_vars())

    if not base.dispatcher.exist_path(environ):
        reference = getattr(app, setting.default_controller)
        reference.default(webinfo.request, webinfo.response)
    else:
        reference = base.dispatcher.find_object(app, environ)
        if callable(reference):
            reference(webinfo.request, webinfo.response)
        else:
            if callable(reference.default):
                reference.default(webinfo.request, webinfo.response)

    return webinfo.response.push()
application = base.exception.ExceptionMiddleware(application)


