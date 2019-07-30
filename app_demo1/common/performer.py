# -*- coding: utf-8 -*-
from app_demo1.common.api_test import Apiclient
from app_demo1.common.tool_func import *
from app_demo1 import config
from app_demo1.common.database_con import  DataManager

class ApiPerformer():
    def __init__(self,file,dbtable):
        self.all_cases = import_api_cases(file)
        self.table=dbtable

    def run(self):
        result=[]
        for case in self.all_cases:
            print(case)
            client = Apiclient(config_build("wuliu",case))
            re=client.test()
            self.save_result(re)  #每执行完一条case就存储到数据库
            result.append(re)
        print(result)
        return result

    def save_result(self,apiresult):
        db=DataManager()
        db.exec_by_sql()


class UiPerformer():
    pass

if __name__=="__main__":
    cc=ApiPerformer("tmpfile//interface_wl.xlsx",'rr')
    print(cc.run())