import os,datetime
file_list = os.listdir("./")

tt = datetime.datetime.now()
dd = str(tt).split(" ")
print(dd[0])

print(os.path.abspath('.'))
os.chdir("../")
print(os.path.abspath('.'))
os.chdir("tmpfile")
print(os.path.abspath('.'))