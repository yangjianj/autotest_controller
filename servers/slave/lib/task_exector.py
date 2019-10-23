# -*- coding: utf-8 -*-
import config
from lib.runner import UiRunner,ApiRunner

class Exector():
    def __init__(self):
        pass

    def task_handler(self,task):
        #{'id':1256635665,'type':'ui','data':{'version':'0.0.1','function':'login'}}
        #{'id':5662356461,'type':'ui','data':{'version':'0.0.1','case':[csv-row1,csv-row1,]}}
        if task['type'] == 'ui':
            self.run_ui(task['data'])
        elif task['type'] == 'api':
            self.run_api(task['data'])
        self.finish_task()

    def run_ui(self,task):
        UiRunner()

    def run_api(self,task):
        ApiRunner()

    def finish_task(self,task):
        pass

    def upload_report(self,report):
        pass
