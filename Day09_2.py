"""
数据准备
"""
from pymysql import Connection
#引入链接功能

#获取MySql 数据库的链接对象
conn = Connection(
    host = "localhost",
    port= 3306,
    user="root",
    password="123456",
    autocommit = True#设置数据更改自动确认
)
print(conn.get_server_info())

conn.select_db("test01")

#建立游标对象来使用数据库
cursor = conn.cursor()


#自己的方法
f = open("D:\software\pycharm\code\数据\shoping.txt","r",encoding="UTF-8")
record_date = f.readlines()

for line in record_date:
    line.strip("\n")
    print(line)
    chart = line.split(",")
    print(f"{chart}{chart[0]},type = {type(chart)}")
    sql = f"insert into orderss(order_date,order_id,money,provine) value('{chart[0]}','{chart[1]}','{float(chart[2])}','{chart[3]}')"
    cursor.execute(sql)



conn.close()
f.close()
# print(record_date[0]) #2011-01-01,asc_sef_123_q123wsj10,680,湖南省
# print(type(record_date[0]))   #<class 'str'>





