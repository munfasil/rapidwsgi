from mako.template import Template
import setting

def default(request, response):
    mytemplate = Template(filename=setting.view_dir+"home.html")
    output = mytemplate.render(data="1")
    c=str(request.form())
    response.set_content(c)
    response.set_content_type("text/html")
    
def test(request, response):
    response.set_content(request.http_vars_dump())
    response.set_content_type("text/html")



