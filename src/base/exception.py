# import the helper functions we need to get and render tracebacks
from sys import exc_info
from traceback import format_tb
from mako.template import Template
from mako.lookup import TemplateLookup
import setting

class ExceptionMiddleware(object):
   
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
       
        application = None
       
        try:
            application = self.app(environ, start_response)
            for item in application:
                return item
        except:
            e_type, e_value, tb = exc_info()
            traceback = ['Traceback (most recent call last):']
            traceback += format_tb(tb)
            traceback.append('%s: %s' % (e_type.__name__, e_value))
          
            try:
                start_response('500 INTERNAL SERVER ERROR', [
                               ('Content-Type', 'text/html')])
            except:
                pass
            mylookup = TemplateLookup(directories=[setting.template_dir])
            mytemplate = Template(filename=setting.template_dir+"error.html",lookup=mylookup)
            output = mytemplate.render(data=traceback,trace=setting.enable_trace)
            return output.encode("utf8")

        #close request
        if hasattr(application, 'close'):
            application.close()
