#coding=utf-8
import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("http://www.lianjia.com")
#########百度输入框的定位方式##########
#通过id方式定位
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/span").click()
browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/input").send_keys("武汉")
print(time.time())
try:
	time.sleep(5)
	browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/a").click()
except Exception as e:
	print(11111111)
print(time.time())
handles = browser.window_handles
print(len(handles))
for i in handles:
	print(i)
	browser.switch_to.window(i)
#browser.close()
#browser.quit()