#
def hello(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    #return ['Hello !!! world!\n']
    aaa = environ["QUERY_STRING"]
    return bytes(aaa.replace("&", "\n"), 'utf-8')
    #return aaa.replace("&", "\n")