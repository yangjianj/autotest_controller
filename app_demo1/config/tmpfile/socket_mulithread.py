# -*- coding: utf-8 -*-
import socket
import threading
import struct

class SocketServer():
    def __init__(self,ip,port):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_list = []
        self.ip = ip
        self.port = port

    def run_base(self):
        self.serversocket.bind((self.ip, self.port))
        self.serversocket.listen()  # 最大连接数
        while True:
            # 此行代码会阻塞，将一直等待client的连接
            s_socket, addr = self.serversocket.accept()
            self.socket_list.append(s_socket)
            # 每当客户端连接后启动一个线程为该客户端服务
            threading.Thread(target=self.server_target, args=(s_socket,addr,)).start()

    def run_file_transport(self):
        self.serversocket.bind((self.ip, self.port))
        self.serversocket.listen()  # 最大连接数
        while True:
            # 此行代码会阻塞，将一直等待client的连接
            s_socket, addr = self.serversocket.accept()
            self.socket_list.append(s_socket)
            # 每当客户端连接后启动一个线程为该客户端服务
            threading.Thread(target=self.server_target, args=(s_socket, addr,)).start()

    def download(self,filename):
        f=open(filename,'rb')

    def upload(self,filename):
        f= open(filename,'ab')

    def server_target(self,s_socket,addr):
        content = '连接成功'
        s_socket.send(content.encode('utf-8'))
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            try:
                content = s_socket.recv(2048).decode('utf-8')
                # 如果捕获到异常，则表明该socket对应的客户端已经关闭
                print(content)
            except:
                # 删除该socket
                self.socket_list.remove(s_socket)
                break
        print(str(addr)+'已断开连接')

if __name__ == '__main__':
    ss = SocketServer('0.0.0.0',1234)
    ss.run_base()




