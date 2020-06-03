# -*-coding:UTF-8 -*-
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json,time
from app_demo1.lib.database_con import DataManager
import app_demo1.lib.tool as Tool
import app_demo1.lib.database_model as DataModel
from app_demo1.lib.user_man import UserManager,check_permission
from app_demo1.lib.slave_man import SlaveManager

# Create your views here.
'''
接口包含：用例上传ftp

'''

@csrf_exempt
def get_all_user1(request):
	#序列化返回结果
	print("in get user1")
	data=DataModel.get_all_user()
	return JsonResponse(data,safe=False)

def allow_origin_response(re):    #允许跨域请求设置
	re["Access-Control-Allow-Origin"] = "*"    
	re["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	re["Access-Control-Max-Age"] = "1000"
	re["Access-Control-Allow-Headers"] = "*"
	return re

