# -*-coding:UTF-8 -*-
import xlrd
import xlwt

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

if __name__=='__main__':
    for i in import_api_cases('tmp_for_execrise\\interface.xlsx'):
        print(i)