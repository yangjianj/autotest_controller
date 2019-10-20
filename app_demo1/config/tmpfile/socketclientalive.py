import socket
import sys,time

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
# 连接服务，指定主机和端口
s.connect(('127.0.0.1', 1234))

# 接收小于 1024 字节的数据
msg = s.recv(1024)  #阻塞
print (msg.decode('utf-8'))
index = 0
while(1):
	index = index + 1
	s.send(('this is clientx_%s'%(index)).encode('utf-8'))
	time.sleep(2)
s.close()


