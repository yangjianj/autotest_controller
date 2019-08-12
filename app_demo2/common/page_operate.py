import time
from app_demo2.common.page_handler import Pagehandle

class Operate():
    def __init__(self,website,browser="chrome"):
        self.handler=Pagehandle(browser,website)

    def execute(self,action,element,value=None,page=None,timeout=5):
        try:
            emeth = getattr(self.handler, action)
            re = emeth(element, value, page)
        except Exception as error:
            emeth = None
        if emeth == None:
            try:
                emeth = getattr(self.handler.get_element(element,page),action)
                re = emeth()
            except Exception as error:
                re=None
                print("no method")
        return re

    def login(self):
        pass

    def logout(self):
        pass

    def goto_dashboard(self):
        pass

    def goto_userpage(self):
        pass

if __name__=='__main__':
    pass