# -*- coding: utf-8 -*-
import yaml,time
from app_demo1.config import config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app_demo1.lib.log_manager import LogManager
#from Exception import Custom_exception

#API网站：https://selenium-python-zh.readthedocs.io/en/latest/index.html
class Pagehandler():

    def __init__(self,browser='chrome'):
        self.logger = LogManager("ui")
        #self.website = website
        self.url = None
        self.curr_page = None
        self.curr_element = None

        if browser == "Firefox" or browser == "firefox":
            self.browser=webdriver.Firefox()
        else:
            self.browser = webdriver.Chrome()
        #self.browser.get(config.WEBSITE[website])  #"http://www.baidu.com"
        self.browser.implicitly_wait(10)

    def load_element_location_file(self,website): #website网站名
        try:
            pagefile=open(config.PAGEFILE[website], 'r', encoding="utf-8")
            _page_message = pagefile.read()
            pagefile.close()
            self.pagedata=yaml.load(_page_message)
        except Exception as e:
            self.logger.error('load element yaml file failed')
            self.logger.error(e)

    def _locate_element(self,element,page=None):
        if page == '' or page == None:
            page = self.curr_page
        elif page != self.curr_page:
            self.curr_page = page
        if page == None:
            raise Exception('page is None !')
        type = self.pagedata[page][element]["type"]
        value = self.pagedata[page][element]["value"]
        return [type, value]


    def _update_msg(self,element,page):
        if page == '' or page == None:   #case中未填写page信息
            pass
        elif page != self.curr_page:
            self.curr_page = page
        if element == '' or element == None:
            pass
        elif element != self.curr_element:
            self.curr_element = element
        return self.curr_element,self.curr_page

    def build_location_by_param(self,element,page,param=None):
        #非确定元素根据参数build元素位置信息
        re = self._locate_element(element,page)
        re[1] = re[1]%(param)
        return re

    def find_element_by_location(self,location):
        if location[0]== 'xpath':
            element = self.browser.find_element_by_xpath(location[1])
            return element
        elif location[0]== 'id':
            element = self.browser.find_element_by_id(location[1])
            return element
        elif location[0]== 'css':
            element = self.browser.find_element_by_css_selector(location[1])
            return element
        elif location[0]== 'name':
            element = self.browser.find_element_by_name(location[1])
            return element
        elif location[0] == 'classes_name':
            element = self.browser.find_element_by_class_name(location[1])
            return element
        else:
            raise Custom_exception.WrongLocation

    def get_elements(self,element,page):
        #根据元素位置信息定位元素，返回元素对象list
        curr_element, curr_page = self._update_msg(element, page)
        location = self._locate_element(curr_element, curr_page)
        if location[0] == 'xpath':
            elements = self.browser.find_elements_by_xpath(location[1])
            return elements
        elif location[0] == 'id':
            elements = self.browser.find_elements_by_id(location[1])
            return elements
        elif location[0] == 'css':
            elements = self.browser.find_elements_by_css_selector(location[1])
            return elements
        elif location[0] == 'name':
            elements = self.browser.find_elements_by_name(location[1])
            return elements
        elif location[0] == 'classes_name':
            elements = self.browser.find_elements_by_class_name(location[1])
            return elements
        else:
            raise Custom_exception.WrongLocation

    def get_element(self,element,page=None):
        #way_list = ['xpath','id','name','classes_name','css']
        curr_element,curr_page = self._update_msg(element,page)
        location=self._locate_element(curr_element,curr_page)
        if location[0]== 'xpath':
            re_element = self.browser.find_element_by_xpath(location[1])
            return re_element
        elif location[0]== 'id':
            re_element = self.browser.find_element_by_id(location[1])
            return re_element
        elif location[0]== 'css':
            re_element = self.browser.find_element_by_css_selector(location[1])
            return re_element
        elif location[0]== 'name':
            re_element = self.browser.find_element_by_name(location[1])
            return re_element
        elif location[0] == 'classes_name':
            re_element = self.browser.find_element_by_class_name(location[1])
            return re_element
        else:
            raise Custom_exception.WrongLocation

    def open_newpage(self,url):
        js = 'window.open(%s);'%(url)
        self.browser.execute_script(js)
        self.switch_to_next_windows()

    #封装WebElement类方法
    def click(self,element,page):
        self.get_element(element,page).click()

    def clear(self,element,page):
        self.get_element(element,page).clear()

    def send_keys(self,element,page,keys):
        self.get_element(element,page).send_keys(keys)

    def double_click(self,element,page):
        self.get_element(element,page).double_click()

    def get_text(self,element,page):
        return self.get_element(element,page).text

    def get_attribute(self,element,page,attr):
        return self.get_element(element,page).get_attribute(attr)

    def is_selected(self,element,page):
        return self.get_element(element,page).is_selected()

    def rect(self,element,page):  #包含元素大小和位置的字典
        return self.get_element(element,page).rect

    #封装Select类方法
    def select_by_index(self,element,page,index):
        ele = self.get_element(element,page)
        return Select(ele).select_by_index(index)

    def select_by_value(self,element,page,value):
        ele = self.get_element(element, page)
        return Select(ele).select_by_value(value)

    def deselect_all(self,element,page):
        ele = self.get_element(element, page)
        return Select(ele).deselect_all()

    #封装ActionChains类方法
    def drag_and_drop(self,page,source,target):
        #source：鼠标按下的源元素；target：鼠标释放的目标元素
        src = self.get_element(source,page)
        dst = self.get_element(target,page)
        ActionChains(self.browser).drag_and_drop(src,dst).perform()

    def move_to_element(self,element,page):
        ele = self.get_element(element,page)
        ActionChains(self.browser).move_to_element(ele).perform()

    # 封装WebDriver类方法
    def implicitly_wait(self,timeout):
        #全局等待元素加载时间，超过此时间还未找到元素则报错
        self.browser.implicitly_wait(timeout)

    def set_page_load_timeout(self,timeout):
        self.browser.set_page_load_timeout(timeout)

    def wait_until_page_contain_element(self,element,page,timeout):
        locate = self._locate_element(element,page)
        if locate[0] == 'id':
            locator = (By.ID, locate[1])
        elif locate[0] == 'xpath':
            locator = (By.XPATH, locate[1])
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),message='wait page contain element timeout')

    def wait_until_page_not_contain_element(self,element,page,timeout):
        locate = self._locate_element(element,page)
        if locate[0] == 'id':
            locator = (By.ID, locate[1])
        elif locate[0] == 'xpath':
            locator = (By.XPATH, locate[1])
        WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located(locator),message='wait page not contain element timeout')

    def get(self,url):
        self.browser.get(url)
        self.browser.maximize_window()

    def maximize_windows(self):
        self.browser.maximize_window()

    def back(self):
        self.browser.back()

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def get_screenshot_as_file(self,filepath):
        self.browser.get_screenshot_as_file(filepath)

    #alert相关方法
    def switch_to_alert(self):
        return self.browser.switch_to_alert()

    def accept(self):
        self.switch_to_alert().accept()

    def dismiss(self):
        self.switch_to_alert().dismiss()

    def get_alert_text(self):
        return self.switch_to_alert().text

    def send_keys_to_alert(self,key):
        self.switch_to_alert().send_keys(key)

    #frame相关方法
    def switch_to(self,type,value=None):
        if type == 'frame':
            self.browser.switch_to.frame(value)
        elif type == 'parent_frame':
            self.browser.switch_to.parent_frame()
        elif type == 'default_content':
            self.browser.switch_to.default_content()
        elif type == 'active_element':
            self.browser.switch_to.active_element()
        elif type == 'alert':
            self.browser.switch_to.alert()
        else:
            raise TypeError


    def switch_to_next_windows(self):
        handles = self.browser.window_handles
        for i in range (len(handles)):
            if handles[i] == self.browser.current_window_handle:
                self.browser.switch_to.window(handles[i+1])
                break

    def switch_to_pre_windows(self,msg):
        handles = self.browser.window_handles
        for i in range(len(handles)):
            if handles[i] == self.browser.current_window_handle:
                self.browser.switch_to.window(handles[i - 1])
                break

if __name__=='__main__':
    web=Pagehandler("baidu","chrome")
    msg={"url":web.url,"element":"搜索框","page":"search","value":"wwwwww","timeout":5,"keys":"sousuo"}
    web.get(msg)
    web.implicitly_wait(msg)
    web.send_keys(msg)
    web.click(msg)
    print(1111)
    web.wait_until_page_contain_element("搜索按钮",5)
    web.wait_until_page_contain_element("测试", 5)
    web.wait_until_page_contain_element("不存在的按钮", 5)
    #time.sleep(5)
    web.close()
    web.quit()
