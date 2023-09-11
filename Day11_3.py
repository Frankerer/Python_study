"""
显示多线程的使用
"""

import time
import threading

def singing():
    while True:
        print("我在唱歌————")
        time.sleep(1)
def danceing():
    while True:
        print("我在跳舞————")
        time.sleep(1)
def drinking(msg):
    while True:
        print(msg)
        time.sleep(1)
def eating(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
#以下内容只在本文件在测试使用设置

    #设置第一个线程
    sing_thread = threading.Thread(target=singing)
    #设置第二个线程
    dance_thread = threading.Thread(target=danceing)
    #设置第三个线程，参数为元组
    drink_thread = threading.Thread(target=drinking,args=("罚一杯",))
    #设置第四个线程，参数为字典
    eating_thread = threading.Thread(target=eating, kwargs={"msg":"吃一顿"})

    #线程执行
    sing_thread.start()
    dance_thread.start()
    drink_thread.start()
    eating_thread.start()