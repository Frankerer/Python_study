"""
文件操作
"""
import time

#打开文件
f = open("D:\software\pycharm\文本文档.txt","r",encoding="UTF-8")
print(type(f))

#读取文件 -read()
print(f"读取部分文件:{f.read(10)}")#读取10字节文件
print(f"读取全部文件:{f.read()}")

#读取文件 -readlines()
lines = f.readlines()#读取文件所有行封装到列表中
print(f"对象的类型是：{type(lines)}")
print(f"对象的内容是：{lines}")

#读取文件 -readline() 一次读取一行内容
line = f.readline()#读取文件一行封装到字符串中
line0 = f.readline()#读取文件一行封装到字符串中
line1 = f.readline()#读取文件一行封装到字符串中
line2 = f.readline()#读取文件一行封装到字符串中
print(f"对象的类型是：{type(line)}")
print(f"对象的类型是：{line}")
print(f"对象的内容是：{line0}")
print(f"对象的内容是：{line1}")
print(f"对象的内容是：{line2}")

for line in f:
    print(line)

#文件关闭
#不关闭文件会被一直占用
f.close()

#自动文件关闭
with open("D:\software\pycharm\文本文档.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)

#x休眠5000万秒
time.sleep(5000)

#读取操作会受之前读取操作的影响，进行继续的读取
with open("D:\software\pycharm\案例.txt","r",encoding="UTF-8") as f:
    #方法一
    i = 0
    for line in f:
        line.split("")#去除开头结尾的空格以及换行符
        list = line.split(" ")
        print(list)
        for x in list:
            if x == "itheima":
                i += 1
    print(i)

    #方法二
    num = f.read().count("itheima")
    print(num)


#打开文件（不存在的文件）
with open("D:\software\pycharm\ text1.txt","w",encoding="UTF_8") as f:
    #写入（write）
    f.write("今天天气真好")
    #文件注入内存(下次可查询)
    f.flush()
    f.read()

f.close()

# 打开文件（存在的文件）使用write写入时会清空原来的内容
with open("D:\software\pycharm\ text1.txt","w",encoding="UTF_8") as f:
    f.write("今天天气不好")

#追写（a）文件，（不存在的文件）
with open("D:\software\pycharm\ text2.txt","a",encoding="UTF_8") as f:
    f.write("今天有钱花")
    f.flush()

#追写（a）文件，（存在的文件）
with open("D:\software\pycharm\ text2.txt","a",encoding="UTF_8") as f:
    f.write("\n金额是100万")
    f.flush()

    f = open("D:/software/pycharm/bill.txt", "r", encoding="UTF_8")
    f1 = open("D:/software/pycharm/bill5.txt.bak", "w", encoding="UTF_8")
    print(type(f))

    for line in f:
        line = line.strip()
        if line.split(",")[4] == "测试":
            continue
        f1.write(line)
        f1.write("\n")

    f.close()
    f1.close()

