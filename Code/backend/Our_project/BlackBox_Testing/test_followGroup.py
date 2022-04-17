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
    req.POST["group_name"] = "CSC4001"

    response = views.followGroup(req)
    json_data = json.loads(response.content)
    data = json_data
    if (response.status_code == 200 and data['ok'] == 1):
        return 1 
    return 0


# wrong will occur
def invalid_group_name():
    req = request("POST")
    req.POST["username"] = "qpr"
    req.POST["group_name"] = "Invalid Group name"

    response = views.followGroup(req)
    json_data = json.loads(response.content)
    data = json_data
    if (b'Invalid Request! Please use Post-request and attach usename and group name.' == response.content):
        return 1 
    return 0

# expect fail because this api only accept post request
def request_with_get():
    req = request("GET")
    req.POST["username"] = "qpr"
    req.POST["id"] = 1

    response = views.followGroup(req)

    if (response.status_code == 200 and b'Only POST-request is accepted!' == response.content):
        return 1
    return 0

# expect fail because the user is not found
def request_with_noone():
    req = request("POST")
    req.POST["username"] = "543625236256t34r34c4325424######"
    req.POST["id"] = 1

    response = views.followGroup(req)
    if (b'Invalid Request! Please use Post-request and attach usename and group name.' == response.content):
        return 1
    return 0

def test():
    if not (normal_test1() == 1):
        return 0
    if not (invalid_group_name() == 1):
        return 0
    if not (request_with_get() == 1):
        return 0
    if not (request_with_noone() == 1):
        return 0

    return 1
