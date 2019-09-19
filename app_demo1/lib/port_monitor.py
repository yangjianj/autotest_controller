import socket
import threading
import time

class PortMonitor(threading.Thread):
    def __init__(self):
        pass

    def testconn(self,host,port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(3)
        connect_result = False
        try:
            sk.connect((host,port))
            print(host + " Server is " + str(port) + " connect")
            connect_result = True
        except Exception as error:
            print(error)
            print(host + " Server is " + str(port) + " not connect!")
        finally:
            sk.close()
        return connect_result

    def test(self,ip,port):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        self.testconn(ip, port)

    def run(self):
        while True:
            print(time.strftime('%Y-%m-%d %H:%M:%S'))
            self.test()
            time.sleep(5)

if __name__ == '__main__':
    PortMonitor().test('127.0.0.1',8090)