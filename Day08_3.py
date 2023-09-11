"""
*********
案例
*********
"""
from pyecharts.charts import Bar


"""
数据准备
"""
import random

f = open("D:\software\pycharm\code\数据\shoping01.txt","w",encoding="UTF-8")

date = "2011-01-01"
for x in range(10,20):
    str = "asc_sef_123_q123wsjwf"
    str01 = str.replace("wf",f"{x}")
    if x > 15:
        money = x*10 + 200 * random.randint(1,10) - x
        f.write(f"date:{date},order_id:{str01},money:{money},province:省\n")
    else:
        money = x * 10 + 100*random.randint(1, 10) - x * 2
        f.write(f"date:{date},order_id:{str01},money:{money},province:省\n")


f.close()



#自己的方法
f = open("D:\software\pycharm\code\数据\shoping.txt","r",encoding="UTF-8")
record_date = f.readlines()
date = []
id = []
money = []
province = []
for line in record_date:
    line.strip("\n")
    chart = line.split(",")
    date.append(chart[0])
    id.append(chart[1])
    money.append(int(chart[2]))
    province.append(chart[3])
    # print(line)   #2011-01-01,asc_sef_123_q123wsj10,680,湖南省
    # print(type(line)) #<class 'str'>

f.close()
# print(record_date[0]) #2011-01-01,asc_sef_123_q123wsj10,680,湖南省
# print(type(record_date[0]))   #<class 'str'>









