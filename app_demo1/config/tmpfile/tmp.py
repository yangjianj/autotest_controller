import sys,io,datetime,time
import threading

def test():
    while(1):
        print(1111)
        time.sleep(3)


threading.Thread(target = test,args=()).start()
print(123454)
time.sleep(5)
print(98987)


