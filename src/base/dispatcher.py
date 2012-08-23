def find_object(obj,environ):
        path_info = environ.get('PATH_INFO', '')
        if not path_info or path_info == '/':
            # We've arrived!
            return obj
        # PATH_INFO always starts with a /, so we'll get rid of it:
        path_info = path_info.lstrip('/')
        # Then split the path into the "next" chunk, and everything
        # after it ("rest"):
        parts = path_info.split('/', 1)
        next = parts[0]
        if len(parts) == 1:
            rest = ''
        else:
            rest = '/' + parts[1]
        # Hide private methods/attributes:
        assert not next.startswith('_')
        # Now we get the attribute; getattr(a, 'b') is equivalent
        # to a.b...

        next_obj = getattr(obj, next)
        # Now fix up SCRIPT_NAME and PATH_INFO...
        environ['SCRIPT_NAME'] += '/' + next
        environ['PATH_INFO'] = rest
        # and now parse the remaining part of the URL...
        return find_object(next_obj, environ)

    
def exist_path(environ):
    path_info = environ.get('PATH_INFO', '')
    if not path_info or path_info == '/':
        return None
    else:
        return True

         
