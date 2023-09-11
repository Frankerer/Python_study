#######################################################
"""
布尔类型数据

True = 1
False = 0

"""
#定义
bool_1 = True
bool_2 = False
print(bool_1,type(bool_1))
print(bool_2,type(bool_2))

# 比较运算符的使用
# == , !=, >, <, >=, <=
num1 = 10
num2 = 20
print(f"10 == 20的结果是{num1 == num2}")
print(f"10 == 20的结果是{num1 == 20}")
print(f"10 != 20的结果是{num1 != num2}")
print(f"10 >= 20的结果是{num1 >= num2}")
print(f"10 <= 20的结果是{num1 <= num2}")
print(f"10 < 20的结果是{num1 < num2}")
print(f"10 > 20的结果是{num1 > num2}")

num3 = "wang"
num4 = "wan"
print(f"wang != wan的结果是{num3 != num4}")
print(f"wang < wan的结果是{num3 < num4}")

#######################################################
#if语句的使用
age = int(input("输入你的年龄"))
if age >=50 :
    print("年龄>=50")#缩进不可省略
elif age >=30 :
    print("年龄>=30")#缩进不可省略
else:
    print("年龄<30")#缩进不可省略
print("拜拜")

num = 10
if int(input("请输入猜想数据")) == num:
    print("对")
elif int(input("再试一次")) == num:
    print("对")
elif int(input("最后一次")) == num:
    print("对")
else:
    print("结束")

age = int(input("输入年龄"))
year = int(input("输入入职时间"))
level = int(input("级别"))
if age >= 18:
    print("年龄初次符合")
    if age <= 30:
        print("年龄达标")
        if year > 2:
            print("可以领取")
        elif level > 3:
            print("可以领取")
        else:
            print("不可以")
    else:
        print("年龄二次审核不过关")
else:
    print("年龄不过关")

#猜测数字

import random
num = random.randint(1,10)
guss_num = int(input("第一次输入数字"))
if guss_num!= num:
    if guss_num >= num:
        print("大了,重试")
    elif guss_num <= num:
        print("小了，重试")

    guss_num = int(input("第二次输入数字"))
    if guss_num != num:
        if guss_num >= num:
            print("大了,重试")
        elif guss_num <= num:
            print("小了，重试")

    guss_num = int(input("第三次输入数字"))
    if guss_num != num:
        if guss_num >= num:
            print("大了,重试")
        elif guss_num <= num:
           print("小了，重试")
        else:
          print("第三次正确")
    else:
        print("第二次正确")
else:
    print("第一次正确")









