# -*- coding: utf-8 -*-
import time,json
import threading
from app_demo1.lib.reques import Reques
from jsonschema import validate

#接口类
class Apiclient():
	def __init__(self,mrequest):
		self.url=mrequest["url"]
		self.method=mrequest["method"]
		self.reparam=mrequest["reparam"]
		self.redata=mrequest["redata"]
		self.headers=mrequest["headers"]
		self.expected=mrequest["expected"]
		self.requ=Reques()
		self.response=[]

	def test(self):
		if self.method=='POST' or self.method=='post':
			result=self.requ.post(url=self.url,redata=self.redata,reparam=self.reparam,headers=self.headers)
		elif self.method=='GET' or self.method=='get':
			result=self.requ.get(url=self.url,headers=self.headers,parms=self.reparam)
		elif self.method=='PUT' or self.method=='put':
			result=self.requ.putfile(url=self.url,params=self.reparam,headers=self.headers)
		elif self.method=='DELETE' or self.method=='delete':
			result=self.requ.delfile(url=self.url,params=self.reparam,headers=self.headers)
		else:
			result={"error":"method not in post,get,put,delete"}
		if ("re" in result) and ("response" in result["re"]):
			print(result)
			test_result=self.response_check(json.loads(result["re"]["response"]),self.expected)
			result["re"]["test_result"]=test_result
		return  result

	def test_multi(self,thread_num):
		t_list=[]
		t_re=[]
		time_start = time.time()
		for i in range(thread_num):
			t=Multiclient(self.test,())
			t_list.append(t)
			t.start()
		time_run = time.time()
		for t in t_list:
			t.join()
			t_re.append(t.get_result())
		time_end = time.time()
		result = {"time":time_end-time_start,"time_run":time_run-time_start,"data":t_re}
		return result

	def response_check(self,data,template):
		#type(data)=dict ; typetemplate=dict
		try:
			validate(instance=data, schema=template)    #return None
			return 'passed'
		except Exception as e:
			return 'failed : '+str(e)

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
	jj={}
	url="http://127.0.0.1:8090/get_all_user"
	jj["url"]="http://127.0.0.1:8090/get_reuqet_json"
	jj["method"]='post'
	jj["redata"]=json.dumps({'username':'name0','password':'pass'})
	jj["reparam"] = {'username': 'name1', 'password': 'pass'}
	jj["expected"]={"type":"object",
	                "properties":{
		                "re_data":{"type":"string"}
	                }}
	headers={}
	#headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
	headers['Content-Type']='application/json; charset=UTF-8'
	headers['Cookie'] = "sessionid=kcgf0uphjyzz6ntnqu29c7adjud03z89"
	jj["headers"]=headers
	client1=Apiclient(jj)
	t_list.append(client1.test())
	#re=client1.test()
	re=client1.test_multi(100)
	print(re['time_run'])
	print(re['time'])



