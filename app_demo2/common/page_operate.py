import time
from app_demo2.common.page_handler import Pagehandle
from app_demo1.common.log_manager import LogManager

class Operate():
    def __init__(self,website,browser="chrome"):
        self.handler=Pagehandle(browser,website)
        self.logger = LogManager("ui")

    def execute(self,action,element,value=None,page=None):
        try:
            emeth = getattr(self.handler, action)
            re = emeth(element, value, page)
        except Exception as error:
            self.logger.error('not find method in class Pagehandle continue search in WebElement ')
            emeth = None
        if emeth == None:
            try:
                emeth = getattr(self.handler.get_element(element,page),action)
                re = emeth()
            except Exception as error:
                self.logger.error('not find method in class WebElement raise error')
                re=None
        return re

#常用固定操作
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