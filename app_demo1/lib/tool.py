# -*-coding:UTF-8 -*-
import os,xlrd,xlwt
from xlutils.copy import copy
import time,datetime
import json
from app_demo1.config import config

#导入excel中接口测试用例
def import_excel_data(path,sheetname):
    result=[]
    workbook = xlrd.open_workbook(path)
    #sheet= workbook.sheet_by_index(0)    #默认取第一个sheet
    sheet = workbook.sheet_by_name(sheetname)
    nrows=sheet.nrows
    ncols=sheet.ncols
    for row in range(0,nrows):
        tmp=[]
        for col in range(0,ncols):
            tmp.append(sheet.cell(row,col).value)
        result.append(tmp)
    return result

def export_data(data,sheet,path):
    if os.path.exists(path):
        oldbook = xlrd.open_workbook(path)
        allsheet = oldbook.sheet_names()
        newbook = copy(oldbook)
        if sheet not in allsheet:
            newsheet=newbook.add_sheet(sheet)
            used_nrows = 0
        else:
            newsheet = newbook.get_sheet(sheet)
            used_nrows = newsheet.last_used_row+1
        for i in range(len(data)):
            for j in range(len(data[i])):
                newsheet.write(used_nrows + i, j, data[i][j])
    else:
        newbook = xlwt.Workbook()
        newsheet = newbook.add_sheet(sheet)
        for i in range (len(data)):
            for j in range (len(data[i])):
                newsheet.write(i,j,data[i][j])
    newbook.save(path)


def config_build(type,conf,dst="taobao"):
    result = {}
    if type == "tuling":    #for class Apiclient
        template= config.tuling_request_data
        template["perception"]["inputText"]["text"]=conf[8]
        result["url"]=conf[4]
        result["method"]=conf[7]
        result["data"]=template
        result["headers"]= config.headers
    if type =="taobao":
        template = config.taobao_querystring
        template["q"] = conf[8]
        result["url"] = conf[4]
        result["method"] = conf[7]
        result["qstring"] = template
        result["payload"] = '{}'
        result["headers"] = config.headers
        print(result)
    if type =="wuliu":
        result["url"] = conf[6]
        result["method"] = conf[9]
        result["reparam"] = json.loads(conf[10].replace('\n', ''))
        result["redata"] = json.dumps('{"key":"val"}')
        result["headers"] = config.headers
        result["expected"] = json.loads(conf[11].replace('\n', ''))
    return result

def record_time(func):    #计时器
    def inner(*args,**kargs):
        result={}
        start_time=datetime.datetime.now()
        re=func(*args,**kargs)
        end_time = datetime.datetime.now()
        result["re"] = re
        result["start-time"]=start_time
        result["end-time"] = end_time
        result["spend"]=end_time-start_time
        return result
    return inner

def create_suite_dir(type,suitename):
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    str = type+suitename+timestr
    os.makedirs(os.path.join(config.UI_RESULT_DIR, str))
    return os.path.join(config.UI_RESULT_DIR, str)

def create_case_dir(suitedir,caseid):
    os.makedirs(os.path.join(suitedir,caseid))
    return os.path.join(suitedir,caseid)


if __name__=='__main__':
    data = [[123,222,333,22,55],['dgiwseh','uhsgfch','jhsih']]
    export_data(data,'test122',"..//log//sss.xlsx")
