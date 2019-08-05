import selenium
import yaml
from app_demo1 import config
from selenium import webdriver
from Exception import Custom_exception

class Pagehandle():

    def __init__(self,browser,web):
        if browser == "Firefox":
            self._browser=webdriver.Firefox()
        else:
            self._browser = webdriver.Chrome()
        self._browser.get(config.WEBSITE[web])  #"http://www.baidu.com"
        try:
            pagefile=open(config.PAGEFILE[web], 'r', encoding="utf-8")
            _page_message = pagefile.read()
            pagefile.close()
            self.pagedata=yaml.load(_page_message)
        except Exception as e:
            print(e)

    def _lacate_element(self,page,element):
        try:
            way = self.pagedata[page][element]["type"]
            value = self.pagedata[page][element]["value"]
            return way, value
        except Exception as e:
            return {"error":"can not find element in .yaml"}

    def get_element(self,page,element):
        way_list = ['xpath','id','name','classes_name','css']
        location=self._lacate_element(page,element)
        for i in way_list:
            if i == location[0] and i == 'xpath':
                element = self._browser.find_element_by_xpath(location[1])
                return element
            elif i == location[0] and i == 'id':
                element = self._browser.find_element_by_id(location[1])
                return element
            elif i == location[0] and i == 'css':
                elements = self._browser.find_elements_by_css_selector(location[1])
                return elements
            elif i == location[0] and i == 'name':
                element = self._browser.find_element_by_name(location[1])
                return element
            elif i == location[0] and i == 'classes_name':
                elements = self._browser.find_elements_by_class_name(location[1])
                return elements
            else:
                raise Custom_exception.WrongLocation


    def click(self,page,element):
        self.get_element(page,element).click()

    def sendkeys(self,page,element,keys):
        self.get_element(page, element).sendkeys(keys)

    def double_click(self):
        pass

    def mouse(self):
        pass

if __name__=='__main__':
    pass