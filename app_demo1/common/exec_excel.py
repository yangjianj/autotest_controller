# -*-coding:UTF-8 -*-
import xlrd
import xlwt
import json
from app_demo1 import config

def import_api_cases(path):
    result=[]
    workbook = xlrd.open_workbook(path)
    sheet= workbook.sheet_by_index(0)    #默认取第一个sheet
    nrows=sheet.nrows
    ncols=sheet.ncols
    for row in range(2,nrows):
        tmp=[]
        for col in range(0,ncols):
            tmp.append(sheet.cell(row,col).value)
        result.append(tmp)
    return result

def import_ui_cases(path):
    pass

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
        result["url"] = conf[4]
        result["method"] = conf[7]
        result["qstring"] = json.loads(conf[8])
        result["payload"] = json.dumps('{"key":"val"}')
        result["headers"] = config.headers
    return result

if __name__=='__main__':
    for i in import_api_cases('tmp_for_execrise\\interface_tb.xlsx'):
        print(i)