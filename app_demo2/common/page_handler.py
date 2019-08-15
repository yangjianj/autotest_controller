# -*- coding: utf-8 -*-
import yaml
from app_demo1.config import config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from app_demo1.common.log_manager import LogManager
#from Exception import Custom_exception

#API网站：https://selenium-python-zh.readthedocs.io/en/latest/index.html
class Pagehandle():

    def __init__(self,website,browser,timeout=5):
        self.logger = LogManager("ui")
        self.curr_page = None

        if browser == "Firefox" or browser == "firefox":
            self.browser=webdriver.Firefox()
        else:
            self.browser = webdriver.Chrome()
        self.browser.get(config.WEBSITE[website])  #"http://www.baidu.com"
        try:
            pagefile=open(config.PAGEFILE[website], 'r', encoding="utf-8")
            _page_message = pagefile.read()
            pagefile.close()
            self.pagedata=yaml.load(_page_message)
        except Exception as e:
            self.logger.error(e)

        self.browser.implicitly_wait(timeout)

    def _locate_element(self,element,page=None):
        if page == '' or page == None:
            page = self.curr_page
        elif page != self.curr_page:
            self.curr_page = page
        try:
            if page == None:
                raise Exception('page is None !')
            type = self.pagedata[page][element]["type"]
            value = self.pagedata[page][element]["value"]
            return type, value
        except Exception as e:
            self.logger.error("can not find element: page:%s element:%s in .yaml"%(page,element))
            self.logger.error(e)
            return None

    def _switch_page(self,page):
        if page == '' or page == None:   #case中未填写page信息
            pass
        elif page != self.curr_page:
            self.curr_page = page
        return self.curr_page

    def get_element(self,element,page=None):
        #way_list = ['xpath','id','name','classes_name','css']
        curr_page = self._switch_page(page)
        location=self._locate_element(element,curr_page)
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

    #封装WebElement类方法
    def click(self,element,page=None):
        self.get_element(element,page).click()

    def clear(self,element,page=None):
        self.get_element(element,page).clear()

    def send_keys(self,element,keys,page=None):
        self.get_element(element,page).send_keys(keys)

    def double_click(self,element,page=None):
        self.get_element(element,page).double_click()

    def text(self,element,page=None):
        return self.get_element(element,page).text

    def get_attribute(self,element,attr,page=None):
        return self.get_element(element,page).get_attribute(attr)

    def is_selected(self,element,page=None):
        return self.get_element(element,page).is_selected()

    def rect(self,element,page=None):  #包含元素大小和位置的字典
        return self.get_element(element,page).rect

    #封装Select类方法
    def select_by_index(self,element,index,page=None):
        ele = self.get_element(element,page)
        return Select(ele).select_by_index(index)

    def select_by_value(self,element,value,page=None):
        ele = self.get_element(element, page)
        return Select(ele).select_by_value(value)

    def deselect_all(self,element,page=None):
        ele = self.get_element(element, page)
        return Select(ele).deselect_all()

    #封装ActionChains类方法
    def drag_and_drop(self,source,target,page=None):
        #source：鼠标按下的源元素；target：鼠标释放的目标元素
        src = self.get_element(source,page)
        dst = self.get_element(target,page)
        ActionChains(self.browser).drag_and_drop(src,dst).perform()

    def move_to_element(self,element,page=None):
        ele = self.get_element(element,page)
        ActionChains(self.browser).move_to_element(ele).perform()

    # 封装WebDriver类方法
    def implicitly_wait(self,timeout=5):
        #全局等待元素加载时间，超过此时间还未找到元素则报错
        self.browser.implicitly_wait(timeout)

    def wait_until_page_contain_element(self,element,timeout,page=None):
        locate = self._locate_element(element,page)
        if locate[0] == 'id':
            locator = (By.ID, locate[1])
        elif locate[0] == 'xpath':
            locator = (By.XPATH, locate[1])
        try:
            ele = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator),message='wait page contain element timeout')
            return ele
        except Exception as e:
            print(e)
            return False

    def wait_until_page_not_contain_element(self,element,timeout,page=None):
        locate = self._locate_element(element,page)
        if locate[0] == 'id':
            locator = (By.ID, locate[1])
        elif locate[0] == 'xpath':
            locator = (By.XPATH, locate[1])
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located(locator),message='wait page not contain element timeout')
            return True
        except Exception as e:
            print(e)
            return False

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

    def get_screenshot_as_file(self, filename):
        self.browser.get_screenshot_as_file(filename)

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

    #############验证方法#############
    def check(self,element,value,page):
        pass



if __name__=='__main__':
    web=Pagehandle("chrome","baidu")
    web.implicitly_wait(5)
    web.send_keys("搜索框","selenium","search")
    web.click("搜索按钮")
    web.wait_until_page_contain_element("搜索按钮",5)
    web.wait_until_page_contain_element("测试", 5)
    web.wait_until_page_contain_element("不存在的按钮", 5)
    #time.sleep(5)
    web.close()
    web.quit()
