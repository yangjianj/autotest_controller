# -*- coding: utf-8 -*-
from app_demo1.common.tool_func import *
from app_demo1.common.log_manager import LogManager
from app_demo2.common.page_operate import Operate
import app_demo1.config.config as config

class UiPerformer():
    def __init__(self, file, dbtable):
        self.all_cases = import_excel_data(file)
        self.table = dbtable
        self.logger = LogManager("ui")

    def run(self):
        result = []
        for case in self.all_cases:
            if case[3] == "open_page":
                Performer = Operate(case[6])
            else:
                re = Performer.execute(case[3],case[5],case[6],case[4])
                #self._save_result(re)  # 每执行完一条case就存储到数据库
                #result.append(re)
        return result

    def set_up(self):
        pass

    def tear_down(self):
        pass

if __name__=="__main__":
    cc=UiPerformer(config.UI_CASE["test"],'rr')
    cc.run()