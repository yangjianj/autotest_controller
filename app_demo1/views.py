# -*-coding:UTF-8 -*-
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json,time
from app_demo1.lib.database_con import DataManager
import app_demo1.lib.tool as Tool
import app_demo1.lib.database_model as DataModel
from app_demo1.lib.user_man import UserManager,check_permission
from app_demo1.lib.workerMan import WorkerManager
from app_demo1.lib.taskMan import TaskManager



def index(reauest):
	return HttpResponse('hello! IN APP1')

def test_model(request):
	print(DataModel.get_yang())
	return render(request, "column3d.html")


def login(request):
	#不使用内置session中间件，使用token方式进行验证
	username = request.POST['username']
	password = request.POST['password']
	if UserManager().check_password(username,password):
		#response= HttpResponseRedirect('/index')
		response = HttpResponse('ok')
		#response.set_cookie('username',username,expires=60*60*24*7)
		request.session["is_login"] = 1
		request.session["username"] = username
		return response
	else:
		return HttpResponse('auth failed')


def logout(request):
	sessionid = request.COOKIES.get("sessionid")
	request.session.delete(sessionid)
	response = HttpResponse('ok')
	return response


@check_permission
def create_user(request):
	username = request.POST["username"]
	password = request.POST["password"]
	userid = request.POST["userid"]
	result = UserManager().create_user(request.POST)
	return JsonResponse(result)

def check_password(request):
	UserManager().check_password(request.POST)




def ajax(request):   #处理前端请求
	result={
			'tag':'正常',
	        'data':[
			         	{
			         		'name' : '大型超市',
			         		'value':[32,19,23,11,7],
			         		'color':'#6b8439'
			         	}
			         ]
			         }
	return HttpResponse(json.dumps(result, ensure_ascii=False))


def get_all_user(request):
	result=[]
	tmpdata={
          "workid": "1",
          "name": "王小虎",
          "role": "admin",
          "project": "core",
          "telephone":"12345"
        }
	db_obj=DataManager()
	re=db_obj.query_users()
	for i in re:
		result.append({"workid":i[2],"name":i[1],"role":i[3],"project":i[4],"telephone":i[5]})
	return HttpResponse(json.dumps(str(result), ensure_ascii=False))


def get_all_user1(request):
	#序列化返回结果
	print("in get user1")
	data=DataModel.get_all_user()
	return JsonResponse(data,safe=False)


def update_user(request):
	result=[]
	db_obj=DataManager()
	result=db_obj.update_user(request.POST["name"],request.POST["workid"],request.POST["role"],request.POST["project"],request.POST["telephone"],)
	return HttpResponse(json.dumps(str(result), ensure_ascii=False))

def get_reuqet_json(request):
	print(request.body.decode())
	#re_data=json.loads(request.body)
	#print(re_data['username'])
	result={'status':200,'re_data':'123456789'}

	return HttpResponse(json.dumps(result, ensure_ascii=False))

def vue_elem(request):
	return render(request,"test_element.html")

def task_status_update(request):   #slave向master更新任务完成状态
	pass


def slave_heartbeat(request):
	print(request.body)
	body = json.loads(request.body.decode())
	ip = body["ip"]
	timestamp = body["timestamp"]
	status = None
	if 'status' in body:
		status = body["status"]
	re = WorkerManager().update_timestamp(ip,timestamp,status)
	if re == True:
		result =  {'status': 'true'}
	else:
		result = {'status': 'false',"message":re["message"]}
	return HttpResponse(json.dumps(result, ensure_ascii=False))


def task_update(request):
	print(request.body)
	body = json.loads(request.body.decode())
	ip = body["ip"]
	timestamp = body["timestamp"]
	task = body["task"]



def create_task(request):
	body = json.loads(request.body.decode())
	tm= TaskManager()
	tm.create_task()


def add_cases_to_task(request):
	body = json.loads(request.body.decode())
	tm = TaskManager()
	tm.add_cases_to_task()
