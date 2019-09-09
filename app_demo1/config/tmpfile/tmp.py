import sys,io,datetime,time
import csv
with open('ddt_test_001.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row)

