
# rapidWSGI                                      *

## Description
Project	: rapidWSGI - A minimal addon for WSGI Framework


## Features
*Supports Model View Controller.
*Mako template libary included.

## Installation procedure:
1. Configure WSGI for apache. Download mod_wsgi from http://code.google.com/p/modwsgi/wiki/DownloadTheSoftware?tm=2	

In httpd.conf add this line to load this module
```
LoadModule wsgi_module modules/mod_wsgi.so

rapidWSGI apache configuration
```

2. Please set the path according to your public html paths.
```
# Points to the start script
WSGIScriptAlias /rapidwsgi C:/wamp/www/rapidwsgi/src/index.wsgi

<Directory C:/wamp/www/rapidwsgi/src>
Order allow,deny
Allow from all
</Directory>

#Set the alias for static contents
Alias /static C:/wamp/www/rapidwsgi/src/static/
```
3)rapidWSGI config

File:src/index.wsgi
```
#includes the path of rapidWSGI to sys	
path='C:/wamp/www/rapidwsgi/src/'

File:src/setting.py
#set the template directory path
template_dir="C:/wamp/www/rapidwsgi/src/template/"
```
