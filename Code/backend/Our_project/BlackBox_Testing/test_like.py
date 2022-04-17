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


# normal test with like a question => expect return with status_code == 200 and ok == 1
def normal_test1():
    req = request("POST")
    req.POST["username"] = "qpr"
    req.POST["id"] = 1
    req.POST['type'] = 0

    response = views.like(req)
    json_data = json.loads(response.content)
    data = json_data
    if (response.status_code == 200 and data['ok'] == 1):
        return 1 
    return 0

# normal test with like an Answer => expect return with status_code == 200 and ok == 1
def normal_test2():
    req = request("POST")
    req.POST["username"] = "qpr"
    req.POST["id"] = 1
    req.POST['type'] = 1

    response = views.like(req)
    json_data = json.loads(response.content)
    data = json_data
    if (response.status_code == 200 and data['ok'] == 1):
        return 1 
    return 0

# expect fail because this api only accept post request
def request_with_get():
    req = request("GET")
    req.POST["username"] = "qpr"

    response = views.like(req)

    if (response.status_code == 200 and b'Only POST-request is accepted!' == response.content):
        return 1
    return 0

# expect fail because the user is not found
def request_with_noone():
    req = request("POST")
    req.POST["username"] = "ruewioihfiwjfbwjebhjrwhe2131293hur"

    response = views.like(req)
    print(response.content)
    if (b'Invalid input!' == response.content):
        return 1
    return 0

def test():
    if not (normal_test1() == 1):
        return 0
    if not (normal_test2() == 1):
        return 0
    if not (request_with_get() == 1):
        return 0
    if not (request_with_noone() == 1):
        return 0

    return 1
