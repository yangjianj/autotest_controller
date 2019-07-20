#coding:utf-8
import sqlite3
conn = sqlite3.connect('dbtest.db')
cc = conn.cursor()
#cc.execute("insert into Users(name,workid)values('alicen','f12345')")
for i in range (100):
    name1=str(i)+'alicen'
    workid1=str(i)+'f884395'
    #cc.execute("insert into Users(name,workid)values('%s','%s')"%(name1,workid1))

print(cc)
re=cc.execute("select * from Users")
for i in re:
    print(i)

conn.commit()
conn.close()