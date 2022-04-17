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


# test valid input with search scope ALL
def normal_test1():
    req = request("POST")
    req.POST["content"] = "what's "
    req.POST["scope"] = "All"

    response = views.searchQuestion(req)
    json_data = json.loads(response.content)
    length = len(json_data)    # means it got search result
    if (response.status_code == 200 and length > 0):
        return 1
    return 0

# test valid input with search scope of group
def normal_test2():
    req = request("POST")
    req.POST["content"] = "what's "
    req.POST["scope"] = "CSC4001"

    response = views.searchQuestion(req)
    json_data = json.loads(response.content)
    length = len(json_data)    # means it got search result
    if (response.status_code == 200 and length > 0):
        return 1
    return 0

# test valid input with search scope of group
def normal_test3():
    req = request("POST")
    req.POST["content"] = "what's "
    req.POST["scope"] = "CSC4001|Project"

    response = views.searchQuestion(req)
    json_data = json.loads(response.content)
    length = len(json_data)    # means it got search result
    if (response.status_code == 200 and length > 0):
        return 1
    return 0

# search with empty content
def invalid_search1():
    req = request("POST")
    req.POST["content"] = ""
    req.POST["scope"] = "All"

    response = views.searchQuestion(req)
    json_data = json.loads(response.content)
    length = len(json_data)    # means it got search result
    if (response.status_code == 200 and length > 0):
        return 1
    return 0

# search with 中文
def test_chinese():
    req = request("POST")
    req.POST["content"] = "什么？"
    req.POST["scope"] = "All"

    response = views.searchQuestion(req)
    json_data = json.loads(response.content)
    length = len(json_data)    # means it got search result
    if (response.status_code == 200 and length > 0):
        return 1
    return 0

def test():
    if not (normal_test1() == 1):
        return 0
    if not (normal_test2() == 1):
        return 0
    if not (normal_test3() == 1):
        return 0
    if not (invalid_search1() == 1):
        return 0
    if not (test_chinese() == 1):
        return 0
    return 1
