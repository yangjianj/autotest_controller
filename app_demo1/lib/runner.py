# -*- coding: utf-8 -*-
from app_demo1.lib.api_test import Apiclient
from app_demo1.lib.tool import *
from app_demo1.lib.database_con import  DataManager
from app_demo1.lib.log_manager import LogManager
from app_demo1.config import config

class ApiPerformer():
    def __init__(self,file,dbtable):
        self.all_cases = import_excel_data(file)
        self.table=dbtable
        self.logger=LogManager("api")

    def run(self):
        result=[]
        for case in self.all_cases[1:]:
            print(case)
            client = Apiclient(config_build("wuliu",case))
            re=client.test()
            re["case"]=case
            print(re)
            self._save_result(re)  #每执行完一条case就存储到数据库
            result.append(re)
        return result

    def _save_result(self,apiresult):
        db=DataManager()
        message =db.save_api_case(apiresult)
        if message != True:
            self.logger.error(message)


class UiPerformer():
    pass

if __name__=="__main__":
    cc=ApiPerformer(config.API_CASE["wuliu"],'rr')
    print(cc.run())