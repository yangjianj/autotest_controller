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
            client = Apiclient(config_build("wuliu",case))
            result.append(client.test())
        print(result)
        self.save_result(result)
        return result

    def save_result(self,result):
        db=DataManager()
        db.exec_by_sql()


class UiPerformer():
    pass

if __name__=="__main__":
    cc=ApiPerformer("tmpfile//interface_wl.xlsx",'rr')
    print(cc.run())