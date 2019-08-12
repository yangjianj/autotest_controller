# -*- coding: utf-8 -*-
from app_demo1.common.tool_func import *
from app_demo1.common.log_manager import LogManager
from app_demo2.common import page_operate

class UiPerformer():
    def __init__(self, file, dbtable):
        self.all_cases = import_excel_data(file)
        self.table = dbtable
        self.logger = LogManager("ui")

    def run(self):
        result = []
        for case in self.all_cases:
            print(case)
            driver = page_operate(case[1],case[2])
            re = driver.test()
            re["case"] = case
            print(re)
            self._save_result(re)  # 每执行完一条case就存储到数据库
            result.append(re)
        return result


if __name__=="__main__":
    cc=UiPerformer("ui.xlsx",'rr')
    print(cc.run())