# import the helper functions we need to get and render tracebacks
from sys import exc_info
from traceback import format_tb
from mako.template import Template
import setting

class ExceptionMiddleware(object):
    """The middleware we use."""

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
            mytemplate = Template(filename=setting.template_dir+"error.html")
            output = mytemplate.render(data=traceback,trace=setting.enable_trace)
            return output.encode("utf8")

        # wsgi applications might have a close function. If it exists
        # it *must* be called.
        if hasattr(application, 'close'):
            application.close()
