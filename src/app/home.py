from mako.template import Template
from mako.lookup import TemplateLookup
import setting

def default(request, response):
    
    mylookup = TemplateLookup(directories=[setting.template_dir])
    mytemplate = Template(filename=setting.template_dir+"home.html",lookup=mylookup)
    output = mytemplate.render(data="1")
    response.set_content(output.encode("utf8"))
    #response.setcontent_type("text/html")
    
def info(request, response):
    mylookup = TemplateLookup(directories=[setting.template_dir])
    mytemplate = Template(filename=setting.template_dir+"test.html",lookup=mylookup)
    output=mytemplate.render(data=request.http_vars())
    response.set_content(output.encode("utf8"))
    #response.setcontenttype("text/html")

def form(request, response):
    mylookup = TemplateLookup(directories=[setting.template_dir])
    mytemplate = Template(filename=setting.template_dir+"form.html",lookup=mylookup)
    
    post_value=request.get_value('post_value')
    
    get_value=request.get_value('get_value')
    
    output = mytemplate.render(post_value=post_value,get_value=get_value,method=request.get_method())
    #c=str(request.form())
    response.set_content(output.encode("utf8"))
    #response.setcontenttype("text/html")


