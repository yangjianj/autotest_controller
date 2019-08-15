#coding=utf-8
from selenium import webdriver
browser=webdriver.Chrome()
browser.get("http://www.lianjia.com")
#########百度输入框的定位方式##########
#通过id方式定位
browser.find_element_by_xpath("kw").send_keys("selenium")

browser.close()
#browser.quit()