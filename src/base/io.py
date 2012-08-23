import cgi
from pprint import pformat

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


