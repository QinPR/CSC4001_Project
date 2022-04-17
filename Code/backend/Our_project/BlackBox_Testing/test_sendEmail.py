from .. import views
import json
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

# test code(). => expect code different in at least 15 times
def normal_test1():
    li = []
    for i in range(0, 15):
        code = views.encode()
        if (code in li):
            return 0
        li.append(code)
    return 1

# test sendEmail => expect code different in at least 15 times
def normal_test2():
    req = request("POST")
    req.POST["email"] = "119010249@link.cuhk.edu.cn"
    response = views.sendEmail(req)
    json_data = json.loads(response.content)
    code = json_data['code']
    if (response.status_code == 200 and code != None):
        return 1
    return 0

# send to an invalid email
def invalid_test():
    req = request("POST")
    req.POST["email"] = "NO_VALID_EMAIL_ADDRESS"
    response = views.sendEmail(req)
    if (response.status_code == 200 and b'Invalid email address!' == response.content):
        return 1
    return 0


def test():
    if not (normal_test1() == 1):
        return 0
    if not (normal_test2() == 1):
        return 0
    if not (invalid_test() == 1):
        return 0
    return 1
