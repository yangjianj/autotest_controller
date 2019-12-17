# -*- coding: utf-8 -*-
import datetime
from app_demo1.models import Api_testcase
from app_demo1.lib.app_serializers import ApiSerializer

class CaseManager():
    def __init__(self):
        pass

    def create_case(self,id,name,project_name,module_name,api_name,api_link,protocol,header,request_data,expected):
        return True

    def update_case(self,id,message):
        keys = message.keys()
        api = Api_testcase.objects.filter(id=id).update(name='yy-1')
        return True

    def delete_case_by_id(self,id):
        api = Api_testcase.objects.filter(id=id).delete()
        return True
    
    def delete_case_by_name(self,name):
        api = Api_testcase.objects.filter(name=name).delete()
        return True
    
    def serach_case_by_id(self,id):
        api = Api_testcase.objects.filter(id=id)
        apijson = ApiSerializer(instance=api, many=True)
        return apijson
    
    def serach_case_by_name(self,name):
        api = Api_testcase.objects.filter(name=name)
        apijson = ApiSerializer(instance=api, many=True)
        return apijson
