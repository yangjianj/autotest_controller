# -*-coding:UTF-8 -*-
import xlrd,xlwt
import json,time,datetime
from app_demo1 import config

#导入excel中接口测试用例
def import_excel_data(path):
    result=[]
    workbook = xlrd.open_workbook(path)
    sheet= workbook.sheet_by_index(0)    #默认取第一个sheet
    nrows=sheet.nrows
    ncols=sheet.ncols
    for row in range(1,nrows):
        tmp=[]
        for col in range(0,ncols):
            tmp.append(sheet.cell(row,col).value)
        result.append(tmp)
    return result

def config_build(type,conf,dst="taobao"):
    result = {}
    if type == "tuling":    #for class Apiclient
        template=config.tuling_request_data
        template["perception"]["inputText"]["text"]=conf[8]
        result["url"]=conf[4]
        result["method"]=conf[7]
        result["data"]=template
        result["headers"]=config.headers
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
        result["start-time"]=str(start_time)
        result["end-time"] = str(end_time)
        result["spend"]=str(end_time-start_time)
        return result
    return inner


if __name__=='__main__':
    for i in import_api_cases('tmp_for_execrise\\interface_tb.xlsx'):
        print(i)
