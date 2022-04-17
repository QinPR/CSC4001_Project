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
    req.POST["username"] = "qpr"

    response = views.main_page(req)
    json_data = json.loads(response.content)
    data = json_data

    index = random.randint(1, len(data)-1)
    blog_test = data['blog' + str(index)]    # verify 1 blog's data randomly
    if not (blog_test):
        return 0
    isLiked = blog_test["isliked"]
    if (isLiked == None):
        return 0
    isfollowed = blog_test['isfollowed']
    if (isfollowed == None):
        return 0
    url = blog_test['url']
    if (url == None):
        return 0
    content = blog_test['content']
    if not (content):
        return 0
    amount_of_answers = blog_test['amount_of_answers']
    if (amount_of_answers == None):
        return 0

    if (response.status_code == 200):
        return 1
    return 0

# expect fail because this api only accept post request
def request_with_get():
    req = request("GET")
    req.POST["username"] = "qpr"

    response = views.main_page(req)

    if (response.status_code == 200 and b'Only POST-request is accepted!' == response.content):
        return 1
    return 0

# expect fail because the user is not found
def request_with_noone():
    req = request("POST")
    req.POST["username"] = "ruewioihfiwjfbwjebhjrwhe2131293hur"

    response = views.main_page(req)
    print(response.content)
    if (b'Invalid Request! Please use Post-request and attach usename.' == response.content):
        return 1
    return 0

def test():
    if not (normal_test1() == 1):
        return 0
    if not (request_with_get() == 1):
        return 0
    if not (request_with_noone() == 1):
        return 0

    return 1
