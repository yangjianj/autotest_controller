# -*- coding: utf-8 -*-
from app_demo1.common.api_test import Apiclient
from app_demo1.common.exec_excel import *
from app_demo1 import config
from app_demo1.common.database_con import  DataManager

class ApiPerformer():
    def __init__(self,file,data_table):
        self.file=file
        self.table=data_table

    def config_build(self,listp):
        param=config.tuling_request_data
        param["perception"]["inputText"]["text"]=listp[7]
        return param

    def run(self):
        result=[]
        all_cases=import_api_cases(self.file)
        for case in all_cases:
            client = Apiclient(case[4], case[7], self.config_build(case),config.headers)
            result.append(client.test())
        print(result)
        self.save_result(result)

    def save_result(self,result):
        db=DataManager()

        db.exec_by_sql()


class UiPerformer():
    pass

if __name__=="__main__":
    cc=ApiPerformer("tmpfile//interface.xlsx",'rr')
    cc.run()