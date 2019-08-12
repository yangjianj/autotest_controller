import time
from app_demo2.common.page_handler import Pagehandle

class Operate():
    def __init__(self,website,browser="chrome"):
        self.handler=Pagehandle(browser,website)

    def method_convert(self,method):

        return 'click'

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