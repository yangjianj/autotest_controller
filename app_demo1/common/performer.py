# -*- coding: utf-8 -*-
from app_demo1.common.api_test import Apiclient
from app_demo1.common.exec_excel import *

class ApiPerformer():
    def __init__(self,file,data_table):
        self.file=file
        self.table=data_table

    def run(self):
        all_cases=import_api_cases(self.file)
        for case in all_cases:
            client = Apiclient(case[4], case[7], case[8])
            client.testapi()

    def save_result(self):
        pass

class UiPerformer():
    pass