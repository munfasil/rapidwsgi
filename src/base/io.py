import cgi
from pprint import pformat

class Dispatcher:
    def find_object(self,obj,environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            
            return obj
        path_info = path_info.lstrip('/')
        parts = path_info.split('/', 1)
        next = parts[0]
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]
        assert not next.startswith('_')
        
        #raise TypeError(next)
        try:
            next_obj = getattr(obj, next)
        except AttributeError:
            __import__(obj.__name__+"."+next)
            next_obj = getattr(obj, next)
            #raise TypeError(obj.__name__+"."+next)
        
            #raise TypeError(obj.__name__+"."+next)
        
        if type(next_obj)=='classobj':
            
            next_obj=next_obj()
             
        
        
        
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest
        
        return self.find_object(next_obj, environ)

    
    def exist_path(self,environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            return None
        else:
            return True

class Request:

    get=None
    
    def __init__(self,environ):
        self.environ=environ
        self.get=self.form()
        
    def form(self):
        form = cgi.FieldStorage(fp=self.environ['wsgi.input'],environ=self.environ)
        return  form

    def method(self):
        return self.environ['REQUEST_METHOD']

    def http_vars_dump(self):
        return pformat(self.environ)
    
    def http_vars_dump_array(self):
        return self.environ

    def http_vars(self):
        return self.environ


    
class Response:

    status="200 OK"
    content_type="text/plain"

    def __init__(self,start_response,content=None):
            self.content=content
            self.start_response=start_response

    def set_content(self,content):
        self.content=content
        
    def set_status(self,status):
        self.status=status
        
    def set_content_type(self,content_type):
        self.content_type=content_type

    def push(self):
        response_headers = [('Content-type', self.content_type),('Content-Length', str(len(self.content)))]
        self.start_response(self.status,response_headers)
        return [self.content]


