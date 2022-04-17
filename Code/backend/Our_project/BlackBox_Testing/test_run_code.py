from .. import views
import json
import random
import requests

class request:
    POST = {}
    GET = {}
    session = {}
    COOKIES = {}
    method = "POST"
    def __init__(self, method):
        self.POST = {}
        self.GET = {}
        self.method = method



# normal test => expect return with status_code == 200
def normal_test1():
    req = request("POST")
    req.POST["source_code"] = "print('hello world')"
    req.POST['lang'] = "Python"

    response = views.run_code(req)
    json_data = json.loads(response.content)
    result = json_data['result']
    
    print(result[0:20])
    if (result[0:20] == "Result: \nhello world"):
        return 1
    return 0

# invalid test 
def invalid_test():
    req = request("POST")
    req.POST["source_code"] = "print('hello world')"
    req.POST['lang'] = "C++"

    response = views.run_code(req)
    json_data = json.loads(response.content)
    result = json_data['result']
    
    if (result[0:20] != "Result: \nhello world"):
        return 1
    return 0

# invalid test 
def GET_test():
    req = request("GET")
    req.POST["source_code"] = "print('hello world')"
    req.POST['lang'] = "Python"

    response = views.run_code(req)
    
    if (b'Only POST-request is accepted!' == response.content):
        return 1
    return 0

# invalid test => it will use the default one: Python
def no_source_code():
    req = request("POST")
    req.POST["source_code"] = "print('hello world')"

    response = views.run_code(req)
    json_data = json.loads(response.content)
    result = json_data['result']
    
    if (result[0:20] == "Result: \nhello world"):
        return 1
    return 0

def test():
    if not (normal_test1() == 1):
        return 0
    if not (invalid_test() == 1):
        return 0
    if not (GET_test() == 1):
        return 0
    if not (no_source_code() == 1):
        return 0

    return 1