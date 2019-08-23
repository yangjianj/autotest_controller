#coding=utf-8
import time
from selenium import webdriver
browser=webdriver.Chrome()
browser.implicitly_wait(5)  #等待元素超时时间
#browser.set_page_load_timeout(5)  #页面加载超时时间
print(time.time())
browser.get("http://www.lianjia.com")
browser.get("http://www.baidu.com")
js='window.open("https://www.sogou.com");'
browser.execute_script(js)
browser.get("http://www.baidu.com") #不会新开页面 会在改变当前handle
print(111111111111111111111)
time.sleep(10)
browser.close()
time.sleep(10)
browser.quit()
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
#browser.close()  #close当前page
#browser.quit()   #关闭browser