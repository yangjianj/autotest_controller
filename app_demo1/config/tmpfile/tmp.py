import sys,io,datetime,time
redirectout = io.StringIO()
redirectout.write("111111111")
print(123)
print(redirectout.getvalue())
print(redirectout.getvalue())

xx=[[1,2,3,4],[5,6,7,8]]

for i,j,y,h in xx:
    print(i,j,y,h)

s1 = datetime.datetime.now()
time.sleep(5)
s2 = datetime.datetime.now()

ss=[]
ss.append([str(s1),str(s2)])
print(ss)

