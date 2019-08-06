# -*- coding: utf-8 -*-
import yaml
from app_demo1 import config
from selenium import webdriver
from app_demo1.common.log_manager import LogManager
#from Exception import Custom_exception

class Pagehandle():

    def __init__(self,browser,web):
        self.logger = LogManager("ui")
        if browser == "Firefox" or browser == "firefox":
            self.browser=webdriver.Firefox()
        else:
            self.browser = webdriver.Chrome()
        self.browser.get(config.WEBSITE[web])  #"http://www.baidu.com"
        try:
            pagefile=open(config.PAGEFILE[web], 'r', encoding="utf-8")
            _page_message = pagefile.read()
            pagefile.close()
            self.pagedata=yaml.load(_page_message)
        except Exception as e:
            self.logger.error(e)

        self.curr_page=None

    def _locate_element(self,element,page=None):
        if page == None:
            page = self.curr_page
        else:
            self.curr_page = page
        try:
            if page == None:
                raise Exception('page is None !')
            way = self.pagedata[page][element]["type"]
            value = self.pagedata[page][element]["value"]
            return way, value
        except Exception as e:
            self.logger.error("can not find element in .yaml")
            self.logger.error(e)
            return None

    def get_element(self,element,page=None):
        #way_list = ['xpath','id','name','classes_name','css']
        location=self._locate_element(element,page)
        if location[0]== 'xpath':
            element = self.browser.find_element_by_xpath(location[1])
            return element
        elif location[0]== 'id':
            element = self.browser.find_element_by_id(location[1])
            return element
        elif location[0]== 'css':
            elements = self.browser.find_elements_by_css_selector(location[1])
            return elements
        elif location[0]== 'name':
            element = self.browser.find_element_by_name(location[1])
            return element
        elif location[0] == 'classes_name':
            elements = self.browser.find_elements_by_class_name(location[1])
            return elements
        else:
            raise Custom_exception.WrongLocation

    def click(self,element,page=None):
        if page == None:
            page=self.curr_page
        self.get_element(element,page).click()

    def clear(self,element,page=None):
        if page == None:
            page=self.curr_page
        self.get_element(element,page).clear()

    def send_keys(self,element,keys,page=None):
        if page == None:
            page = self.curr_page
        self.get_element(element,page).send_keys(keys)

    def double_click(self,element,page=None):
        if page == None:
            page = self.curr_page
        self.get_element(element,page).double_click()

    def mouse(self):
        pass

    def switch_page(self,page):
        self.curr_page=page

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def get_screenshot_as_file(self, filename):
        self.browser.get_screenshot_as_file(filename)

    def get_text(self,element):
        return self.get_element(element,self.curr_page).text

    def page_should_contain_element(self,elemnt,type,timeout=5):
        i =0
        result = None
        while i<timeout:
            try:
                if type == 'id':
                    self.browser.find_element_by_id(elemnt)
                elif type == 'xpath':
                    self.browser.find_element_by_xpath(elemnt)
                result = True
                i = timeout
            except Exception as e:
                result = None
                i = i+1
        return result



if __name__=='__main__':
    web=Pagehandle("chrome","baidu")
    web.send_keys("搜索框","selenium","search")
    web.click("搜索按钮")
