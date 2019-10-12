# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class middle11(MiddlewareMixin):
    def process_request(self, request):
        print("中间件1请求")
        if (request.path == '/test1'):
            return redirect("/index")


    def process_response(self, request, response):
        print("中间件1返回")
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
