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
class Pagehandler():

    def __init__(self,website,browser,timeout=5):
        self.logger = LogManager("ui")
        self.url = config.WEBSITE[website]
        self.curr_page = None
        self.curr_element = None

        if browser == "Firefox" or browser == "firefox":
            self.browser=webdriver.Firefox()
        else:
            self.browser = webdriver.Chrome()
        #self.browser.get(config.WEBSITE[website])  #"http://www.baidu.com"
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

    def get_element(self,element,page=None):
        #way_list = ['xpath','id','name','classes_name','css']
        curr_element,curr_page = self._update_msg(element,page)
        location=self._locate_element(curr_element,curr_page)
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
    def click(self,msg):
        element = msg["element"]
        page = msg["page"]
        self.get_element(element,page).click()

    def clear(self,msg):
        element = msg["element"]
        page = msg["page"]
        self.get_element(element,page).clear()

    def send_keys(self,msg):
        element = msg["element"]
        page = msg["page"]
        keys = msg["keys"]
        self.get_element(element,page).send_keys(keys)

    def double_click(self,msg):
        element = msg["element"]
        page = msg["page"]
        self.get_element(element,page).double_click()

    def text(self,msg):
        element = msg["element"]
        page = msg["page"]
        return self.get_element(element,page).text

    def get_attribute(self,msg):
        element = msg["element"]
        page = msg["page"]
        attr = msg["attr"]
        return self.get_element(element,page).get_attribute(attr)

    def is_selected(self,msg):
        element = msg["element"]
        page = msg["page"]
        return self.get_element(element,page).is_selected()

    def rect(self,msg):  #包含元素大小和位置的字典
        element = msg["element"]
        page = msg["page"]
        return self.get_element(element,page).rect

    #封装Select类方法
    def select_by_index(self,msg):
        element = msg["element"]
        page = msg["page"]
        index = msg["index"]
        ele = self.get_element(element,page)
        return Select(ele).select_by_index(index)

    def select_by_value(self,msg):
        element = msg["element"]
        page = msg["page"]
        value = msg["value"]
        ele = self.get_element(element, page)
        return Select(ele).select_by_value(value)

    def deselect_all(self,msg):
        element = msg["element"]
        page = msg["page"]
        ele = self.get_element(element, page)
        return Select(ele).deselect_all()

    #封装ActionChains类方法
    def drag_and_drop(self,msg):
        source = msg["source"]
        target = msg["target"]
        page = msg["page"]
        #source：鼠标按下的源元素；target：鼠标释放的目标元素
        src = self.get_element(source,page)
        dst = self.get_element(target,page)
        ActionChains(self.browser).drag_and_drop(src,dst).perform()

    def move_to_element(self,msg):
        element = msg["element"]
        page = msg["page"]
        ele = self.get_element(element,page)
        ActionChains(self.browser).move_to_element(ele).perform()

    # 封装WebDriver类方法
    def implicitly_wait(self,msg):
        #全局等待元素加载时间，超过此时间还未找到元素则报错
        timeout = msg["timeout"]
        self.browser.implicitly_wait(timeout)

    def wait_until_page_contain_element(self,msg):
        element = msg["element"]
        page = msg["page"]
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

    def wait_until_page_not_contain_element(self,msg):
        element = msg["element"]
        page = msg["page"]
        timeout = msg['timeout']
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

    def get(self,msg):
        url = msg["url"]
        self.browser.get(url)

    def maximize_windows(self,msg):
        self.browser.maximize_window()

    def back(self,msg):
        self.browser.back()

    def close(self,msg):
        self.browser.close()

    def quit(self,msg):
        self.browser.quit()

    def refresh(self,msg):
        self.browser.refresh()

    def get_screenshot_as_file(self, msg):
        fielpath = msg["filepath"]
        self.browser.get_screenshot_as_file(fielpath)

    def switch_to_alert(self,msg):
        return self.browser.switch_to_alert()

    def accept(self,msg):
        self.switch_to_alert().accept()

    def dismiss(self,msg):
        self.switch_to_alert().dismiss()

    def get_alert_text(self,msg):
        return self.switch_to_alert().text

    def send_keys_to_alert(self,msg):
        key = msg["key"]
        self.switch_to_alert().send_keys(key)

    #############验证方法#############
    def check(self,msg):
        element = msg["element"]
        page = msg["page"]
        pass



if __name__=='__main__':
    web=Pagehandler("baidu","chrome")
    msg={"url":web.url,"element":"搜素框","page":"search","value":"wwwwww","timeout":5,"keys":"sousuo"}
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
