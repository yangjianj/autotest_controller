# -*- coding: utf-8 -*-
import time
import threading
from app_demo1.common.reques import Reques

#接口类
class Apiclient():
	def __init__(self,mrequest):
		self.url=mrequest["url"]
		self.method=mrequest["method"]
		self.qstring=mrequest["qstring"]
		self.payload=mrequest["payload"]
		self.headers=mrequest["headers"]
		self.requ=Reques()
		self.response=[]
		print("in apiclient")
		print(self.qstring)
	def test(self):
		start_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		if self.method=='POST' or self.method=='post':
			result=self.requ.post(url=self.url,payload=self.payload,qstring=self.qstring,headers=self.headers)
		elif self.method=='GET' or self.method=='get':
			result=self.requ.get(url=self.url,headers=self.headers,parms=self.param)
		elif self.method=='PUT' or self.method=='put':
			result=self.requ.putfile(url=self.url,params=self.param,headers=self.headers)
		elif self.method=='DELETE' or self.method=='delete':
			result=self.requ.delfile(url=self.url,params=self.param,headers=self.headers)
		else:
			raise Exception("Invalid method!",self.method)
		end_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		result["start_time"]=start_time
		result["end_time"]=end_time
		return  result

	def test_multi(self,thread_num):
		t_list=[]
		t_re=[]
		time_start=time.time()
		for i in range(thread_num):
			t=Multiclient(self.test,())
			t_list.append(t)
			t.start()
		for t in t_list:
			t.join()
			t_re.append(t.get_result())
		time_end=time.time()
		result={"time":time_end-time_start,"data":t_re}
		return result

class Multiclient(threading.Thread):
	def __init__(self,func,args=()):
		super(Multiclient,self).__init__()
		self.func=func
		self.args=args

	def run(self):
		self.result=self.func(*self.args)

	def get_result(self):
		try:
			return self.result
		except Exception as e:
			return e

def a(x=1):
	time.sleep(5)
	print('sleeping....')
	return 1

if __name__ == '__main__':
	t_list=[]
	t_re=[]
	jj={}
	url="http://localhost:8090/get_all_user/"
	jj["url"]="http://localhost:8090/get_reuqet_json/"
	jj["method"]='post'
	jj["data"]={'username':'name','password':'pass'}
	headers={}
	#headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
	headers['Content-Type']='application/json; charset=UTF-8'
	jj["headers"]=headers
	client1=Apiclient(jj)
	#t_list.append(client1.test())
	re=client1.test()
	#re=client1.test_multi(800)
	print(re)



