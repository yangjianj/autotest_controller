import time
from app_demo2.common.page_handler import Pagehandler
from app_demo1.common.log_manager import LogManager

class Operate():
    def __init__(self,website,browser="chrome"):
        self.handler=Pagehandler(website,browser)
        self.logger = LogManager("ui")

    def execute(self,action,element,value=None,page=None):
        try:
            emeth = getattr(self.handler, action)
            re = emeth(element, value, page)
        except Exception as error:
            self.logger.error('execute failed in class Pagehandle:  action:%s element:%s value:%s page:%s  '%(action,element,value,page))
            print('eeeeeeeeeeeeeeeeeeee')
            emeth = None
        if emeth == None:
            try:
                emeth = getattr(self.handler.get_element(element,page),action)
                re = emeth()
            except Exception as error:
                self.logger.error('execute failed in class webdriver:  action:%s element:%s value:%s page:%s  '%(action,element,value,page))
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