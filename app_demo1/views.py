#coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json,time
from app_demo1.lib.database_con import DataManager
from app_demo1.lib.api_test import Apiclient
import app_demo1.lib.tool as Tool
import app_demo1.lib.database_model as DataModel
from app_demo1.lib.user_manager import UserManager

# Create your views here.

def index(reauest):
	return HttpResponse('hello! IN APP1')

def test1(request):
	return render(request,"test1.html")

def test_inapp(request):
	return render(request,"test_app1.html")

def area2d(request):
	return render(request,"area2d_01.html")

def column3d(request):
	return render(request,"column3d.html")

def test_model(request):
	print(DataModel.get_yang())
	return render(request, "column3d.html")

@csrf_exempt
def login(request):
	#不使用内置session中间件，使用token方式进行验证
	print('in login')
	print(request.POST)
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username,passwod = password)
	print(username,password)
	print('验证结果:',user)
	if user is not None:
		response= HttpResponseRedirect('/index')
		response.set_cookie('token',token,expires=60*60*24*7)
		return response
	else:
		return redirect("/login")

@csrf_exempt
def logout(request):
	response = HttpResponse('ok')
	response.delete_cookie('token')
	return response

@csrf_exempt
def ajax(request):   #处理前端请求
	print(111111111111111)
	print(request.POST)
	print(request.POST["username"])
	print(request.POST["password"])
	print(1111111111111111)
	print(request.body)
	print(222222222222)
	result={
			'tag':'正常',
	        'data':[
			         	{
			         		'name' : '便利店',
			         		'value':[9,12,10,11,16],
			         		'color':'#e0b645'
			         	},
			         	{
			         		'name' : '超市',
			         		'value':[63,42,38,21,14],
			         		'color':'#7876ba'
			         	},
			         	{
			         		'name' : '大型超市',
			         		'value':[32,19,23,11,7],
			         		'color':'#6b8439'
			         	}
			         ]
			         }
	result=HttpResponse(json.dumps(result, ensure_ascii=False))
	result=allow_origin_response(result)
	return result

@csrf_exempt
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
	result=HttpResponse(json.dumps(str(result), ensure_ascii=False))
	result=allow_origin_response(result)
	return result

@csrf_exempt
def get_all_user1(request):
	#序列化返回结果
	print("in get user1")
	data=DataModel.get_all_user()
	return JsonResponse(data,safe=False)


@csrf_exempt
def update_user(request):
	result=[]
	db_obj=DataManager()
	result=db_obj.update_user(request.POST["name"],request.POST["workid"],request.POST["role"],request.POST["project"],request.POST["telephone"],)
	result=HttpResponse(json.dumps(str(result), ensure_ascii=False))
	result=allow_origin_response(result)
	return result

@csrf_exempt
def get_reuqet_json(request):
	print(11111111111111111)
	print(request.body.decode())
	re_data=json.loads(request.body)
	print(re_data['username'])
	result={'status':200,'re_data':'123456789'}
	result=HttpResponse(json.dumps(result, ensure_ascii=False))
	result=allow_origin_response(result)
	return result

def test_api(request):
	re_data = json.loads(request.body)
	client=Apiclient(re_data['url'],re_data['method'],re_data['params'],re_data['headers'])
	client.testapi_multi(100)
	return True

def vue_elem(request):
	return render(request,"test_element.html")



def allow_origin_response(re):    #允许跨域请求设置
	re["Access-Control-Allow-Origin"] = "*"    
	re["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	re["Access-Control-Max-Age"] = "1000"
	re["Access-Control-Allow-Headers"] = "*"
	return re