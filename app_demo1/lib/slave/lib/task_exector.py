# -*- coding: utf-8 -*-
class Exector():
    def __init__(self):
        pass

    def task_handler(self,task):
        if task['type'] == 'ui':
            self.run_ui()
        else:
            self.run_api()
        self.finish_task()

    def run_ui(self):
        pass

    def run_api(self):
        pass

    def finish_task(self):
        pass
