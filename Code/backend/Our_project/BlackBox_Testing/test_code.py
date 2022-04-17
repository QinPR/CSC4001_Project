from .. import views

class request:
    POST = {}
    GET = {}
    method = "POST"
    def __init__(self, method):
        self.POST = {}
        self.GET = {}
        self.method = method

def test():
    req = request("POST")
    li = []
    for i in range(0, 100):
        code = views.encode()
        if (code in li):
            return 0
        li.append(code)
    return 1