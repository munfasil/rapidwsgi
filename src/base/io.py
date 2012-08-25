import cgi
import default
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

    __form=None
    
    def __init__(self,environ):
        self.environ=environ
        self.__form=self.__initform()
        
    def __initform(self):
        form = cgi.FieldStorage(fp=self.environ['wsgi.input'],environ=self.environ)
        return  form

    def get_method(self):
        return self.environ['REQUEST_METHOD']

    def http_vars_dump(self):
        return pformat(self.environ)
    
    def http_vars(self):
        return self.environ
    
    def get_value(self,key):
        
        return self.__form.getvalue(key)
    
    def get_list(self,key):
        
        return self.__form.getlist(key)
    
    def get_form(self):
        
        return self.__form
    
    def haskey(self,key):
        
        return self.__form.has_key(key)
    
    def get_keys(self):
        
        return self.__form.keys() 
    
    
class Response:

    __status=default.RESPONSE_CODE[200]
    __content_type=default.CONTENT_TYPE['html']
    __content=""
    __start_response=None

    def __init__(self,start_response,content=None):
            self.__content=content
            self.__start_response=start_response

    def set_content(self,content):
        self.__content=content
        
    def set_status(self,status):
        self.__status=status
        
    def set_contentype(self,content_type):
        self.__content_type=content_type

    def push(self):
        response_headers = [('Content-type', self.__content_type),('Content-Length', str(len(self.__content)))]
        self.__start_response(self.__status,response_headers)
        return [self.__content]


