import selenium
import yaml
from app_demo1 import config

class Pagehandle():

    def __init__(self):
        _page_message=open(config.pagefile)
        self.pagefile=yaml.load()

    def click(self,page,element):
        pass

    def sendkeys(self,page,element,keys):
        pass

    def double_click(self):
        pass

    def mouse(self):
        pass

if __name__=='__main__':
    pass