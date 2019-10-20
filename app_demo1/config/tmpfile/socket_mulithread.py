# -*- coding: utf-8 -*-
import socket
import threading

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_list = []
def read_from_client(s_socket):
    try:
        return s_socket.recv(2048).decode('utf-8')
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        # 删除该socket
        socket_list.remove(s_socket)

def server_target(s_socket):
    content = '连接成功'
    s_socket.send(content.encode('utf-8'))
    # 采用循环不断地从socket中读取客户端发送过来的数据
    while True:
        content = read_from_client(s_socket)
        print(content)
        if content is None:
            break
        #for client_s in socket_list:
        #    client_s.send(content.encode('utf-8'))

if __name__ == '__main__':
    serversocket.bind(('0.0.0.0', 1234))
    serversocket.listen()  # 最大连接数
    while True:
        # 此行代码会阻塞，将一直等待client的连接
        s_socket, addr = serversocket.accept()
        socket_list.append(s_socket)
        # 每当客户端连接后启动一个线程为该客户端服务
        threading.Thread(target=server_target, args=(s_socket,)).start()
        print("##############")
