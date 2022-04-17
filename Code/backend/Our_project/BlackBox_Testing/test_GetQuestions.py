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
    req.POST["username"] = "QinPR"
    req.POST["question_id"] = 1

    response = views.GetQuestions(req)
    json_data = json.loads(response.content)
    data = json_data

    content = data['content']    
    if not (content):
        return 0
    isliked = data['isliked']
    if (isliked == None):
        return 0
    isfollowed = data['isfollowed']
    if (isfollowed == None):
        return 0
    pic_urls = data['pic_urls']
    if (pic_urls == None):
        return 0
    file_urls = data['file_urls']
    if (file_urls == None):
        return 0
    amount_of_answers = data['amount_of_answers']
    if (amount_of_answers == None):
        return 0
    sub_group_name = data['sub_group_name']
    if (sub_group_name == None):
        return 0
    author_name = data['author_name']
    if (author_name == None):
        return 0
    author_profile = data['author_profile']
    if (author_profile == None):
        return 0

    if (response.status_code == 200):
        return 1
    return 0

# expect fail because this api only accept post request
def request_with_get():
    req = request("GET")
    req.POST["username"] = "qpr"
    req.POST['id'] = 1

    response = views.GetQuestions(req)

    if (response.status_code == 200 and b'Only POST-request is accepted!' == response.content):
        return 1
    return 0

# expect fail because the user is not found
def request_with_noone():
    req = request("POST")
    req.POST["username"] = "ruewioihfiwjfbwjebhjrwhe2131293hur"
    req.POST['id'] = 1

    response = views.GetQuestions(req)
    print(response.content)
    if (b'Invalid Request! Please use Post-request and attach usename and question id.' == response.content):
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
