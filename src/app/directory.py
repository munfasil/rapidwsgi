def __init__(self, request):
    return ""

def default(request, response):
    output = "<html><title>banow framework</title><body><h1>banow framework</h1></body></html>"
    response.set_content(output)
    response.set_content_type("text/html")


def printme(request, response):
    output = "<html><title>banow framework</title><body><h1>hellow</h1></body></html>"
    response.set_content(output)
    response.set_content_type("text/html")


