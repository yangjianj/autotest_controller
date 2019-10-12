# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
import app_demo1.lib.tool as Tool

class UserLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("中间件UserLoginMiddleware请求")
        print(request.path)
        if request.path in ['/login','/index','/admin']:   #login方法不需要经过是否登录判断
            return None
        token = request.COOKIES.get('token')
        if not token:                  #没有token则说明没有登录
            return redirect("/login")
        username = request.POST['username']
        if token != Tool.token_generate(username):
            return redirect("/login")
        else:
            pass
        if (request.path == '/test1'):  #测试
            return redirect("/index")


    def process_response(self, request, response):
        print("中间件UserLoginMiddleware返回")
        return response


class middle2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件2请求")

    def process_response(self, request, response):
        print("中间件2返回")
        return response


class middle3(MiddlewareMixin):
    def process_request(self, request):
        print("中间件3请求")

    def process_exception(self, request, exception):
        if isinstance(exception, ValueError):
            return HttpResponse("404")

    def process_response(self, request, response):
        print("中间件3返回")
        return response
