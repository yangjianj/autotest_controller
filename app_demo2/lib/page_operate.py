import time,json
from app_demo2.lib.page_handler import Pagehandler
from app_demo1.lib.log_manager import LogManager

class Operate():
    def __init__(self,website,browser="chrome"):
        self.handler=Pagehandler(website,browser)
        self.logger = LogManager("ui")

    def execute(self,msg):
        try:
            emeth = getattr(self.handler, msg['action'])
            re = emeth(msg)
        except Exception as error:
            self.logger.error('execute failed in class Pagehandle:  %s'%(json.dumps(msg,ensure_ascii=False)))
            re = False
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