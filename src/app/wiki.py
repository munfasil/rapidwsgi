from mako.template import Template
import setting
import pprint, pickle



def default(request, response):
    mytemplate = Template(filename=setting.view_dir+"home.html")
    output = mytemplate.render(data="1")
    output=request.get.getvalue("page")

    pagename=output.split("/")[1]
    
    if pagename:
        str="sample text"
        f=open(setting.wiki_dir+pagename,"w")
        pickle.dump(f,str)
        f.close()

    f=open(setting.wiki_dir+pagename,"rb")
    data1 = pickle.load(f)
    f.close();

    response.set_content(str(1))
    response.set_content_type("text/html") 
    



