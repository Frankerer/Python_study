"""
客户端开发
"""

import socket

#建立socket对象
socket_client = socket.socket()

#链接服务端
socket_client.connect(("localhost",8888))

while True:
    send_msg = input("输入消息")
    if send_msg == "exit":
        break
    #建立客户端发送消息
    socket_client.send(send_msg.encode("UTF-8"))

    #缓存服务端消息（接收服务端消息）
    recv_data = socket_client.recv(1024)

    print(f"服务端回复消息:{recv_data.decode('UTF-8')}")

#关闭链接
socket_client.close()