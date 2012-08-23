from mako.template import Template
from mako.lookup import TemplateLookup
import setting

def default(request, response):
    mytemplate = Template(filename=setting.view_dir+"home.html")
    output = mytemplate.render(data="1")
    response.set_content(output)
    response.set_content_type("text/html")
