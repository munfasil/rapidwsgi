from mako.template import Template
from mako.lookup import TemplateLookup
import setting

def default(request, response):
    
    mylookup = TemplateLookup(directories=[setting.template_dir])
    mytemplate = Template(filename=setting.template_dir+"home.html",lookup=mylookup)
    output = mytemplate.render(data="1")
    response.set_content(output.encode("utf8"))
    response.set_content_type("text/html")
    
def test(request, response):
    response.set_content(request.http_vars_dump())
    response.set_content_type("text/html")

def form(request, response):
    mytemplate = Template(filename=setting.template_dir+"home.html")
    output = mytemplate.render(data="1")
    c=str(request.form())
    response.set_content(c)
    response.set_content_type("text/html")


