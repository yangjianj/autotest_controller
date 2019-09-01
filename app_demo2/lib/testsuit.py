# -*- coding: utf-8 -*-
import os,sys
import time,datetime
import re,random
from app_demo2.lib.testcase import Testcase
from app_demo1.lib.tool import *
import app_demo1.config.config
from app_demo2.lib.page_operate import Operate
from app_demo1.lib.log_manager import LogManager

class Testsuit():
    #一个testsuit对应一个excel的sheet
    def __init__(self):
        self.casedata = None
        self.operate = None
        self.testcases = []
        self.name = None
        self.result=[]
        self.passed=0
        self.failed=0
        self.spendtime=datetime.datetime.now()-datetime.datetime.now()
        self.setup_rows = []
        self.teardown_rows = []
        self.suite_dir=''
        self.variable={}
        self.logger = LogManager("ui")

    def loadcases(self,excel,suitename):
        self.name = suitename
        self.casedata = import_excel_data(excel,suitename)
        self._data_split_for_suite()

    def _data_split_for_suite(self):
        _curr_case = []
        for row in self.casedata[config.EXCELMAPPING["suitebegine"]:]:
            if row[1] == "SUITE_SETUP":
                self.setup_rows.append(row)
            elif row[1] == "SUITE_TEARDOWN":
                self.teardown_rows.append(row)
            else:
                if _curr_case == []:
                    _curr_case.append(row)
                elif row[config.EXCELMAPPING["用例编号"]] == '' or row[config.EXCELMAPPING["用例编号"]] == _curr_case[-1][
                    config.EXCELMAPPING["用例编号"]]:
                    _curr_case.append(row)
                else:
                    self.testcases.append(Testcase(_curr_case[0:], self.operate))
                    _curr_case.clear()
                    _curr_case.append(row)
            if row is self.casedata[-1]:
                self.testcases.append(Testcase(_curr_case[0:], self.operate))

    def run(self):
        self.suite_dir=create_suite_dir("uitest",self.name)
        self.setup()
        for case in self.testcases:
            self._update_case(case)
            result=case.run()
            if result["re"]["result"] == "passed":
                self.passed += 1
            else:
                self.failed += 1
            self.result.append(result)
            result["re"]["steps"][0][config.EXCELMAPPING["执行时间"]]=str(result["spend"])
            self.spendtime = self.spendtime+result["spend"]
            self._write_result(result["re"]["steps"])
        self.teardown()

    def _update_case(self,case):
        case.operate = self.operate
        case.suite_dir = self.suite_dir
        case.suite_variable = self.variable

    def execute(self,msg):
        msg["value"] = self._data_identify(msg["value"])
        try:
            emeth = getattr(self, msg['action'])
            message = emeth(msg)
            re = {"result": "passed", "message": message}
        except Exception as error:
            message=self.operate.execute(msg)
            re = message
        return re

    def setup(self):
        _setup_result = []
        for i in self.casedata[0:config.EXCELMAPPING["suitebegine"]]:
            _setup_result.append(i)
        for step in self.setup_rows:
            msg = {"action": step[config.EXCELMAPPING["操作"]], "page": step[config.EXCELMAPPING["PageName"]],
                   "element": step[config.EXCELMAPPING["元素名称"]]}
            try:
                msg["value"] = json.loads(step[config.EXCELMAPPING["value"]])
            except Exception as  error:
                msg["value"] = step[config.EXCELMAPPING["value"]]
            result=self.execute(msg)
            _setup_result.append(self._record_result(step, result))
        self._write_result(_setup_result)

    def teardown(self):
        _teardown_result=[]
        for step in self.teardown_rows:
            msg = {"action": step[config.EXCELMAPPING["操作"]], "page": step[config.EXCELMAPPING["PageName"]],
                   "element": step[config.EXCELMAPPING["元素名称"]]}
            try:
                msg["value"] = json.loads(step[config.EXCELMAPPING["value"]])
            except Exception as  error:
                msg["value"] = step[config.EXCELMAPPING["value"]]
            result=self.execute(msg)
            _teardown_result.append(self._record_result(step, result))
        self._write_result(_teardown_result)

    def set_variable(self,msg):
        del msg["action"]
        del msg["page"]
        del msg["element"]
        self.variable.update(msg["value"])

    def open_browser(self,msg):
        self.operate = Operate(msg["value"]["website"], browser=msg["value"]["browser"])
        return self.operate

    def get_variable(self,msg):
        if 'value' in msg:
            key = msg["value"]['value']
            try:
                return self.variable[key]
            except Exception as error:
                return ''
        else:
            return self.variable

    def _data_identify(self,data):
        # type(data) = dict识别输入数据中引用的变量，变量格式<val>
        for item in data:
            if '<' in str(data[item]):  #此行可去除，为减小运算度而保留
                try:
                    val = re.match("^<(\S*)>$", data[item]).group(1)
                    if val in self.variable:
                        data[item] = self.variable[val]
                    else:
                        data[item] = eval(val)

                except Exception as error:
                    pass
        return data

    def _write_result(self,caseresult):
        export_data(caseresult,self.name,os.path.join(self.suite_dir,'test.xlsx'))

    def _record_result(self,step,result):
        step[config.EXCELMAPPING["执行结果"]] = result["result"]
        step[config.EXCELMAPPING["执行信息"]] = str(result["message"])
        if step[config.EXCELMAPPING["输出数据"]] != '':
            result_key = step[config.EXCELMAPPING["输出数据"]]
            self.variable[result_key] = step[config.EXCELMAPPING["执行信息"]]
        return step


if __name__ == '__main__':
    te = Testsuit()
    te.loadcases(config.UI_CASE['test'],"lianjia1")
    print(te.testcases)
    for i in te.testcases:
        print(i.steps)
    te.run()