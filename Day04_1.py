"""
函数进阶
"""

#多返回值

def text_return():
    return 1,"hello",True

x,y,z = text_return()
print(f"{x}\t{y}\t{z}\t")


#函数的传参方式

#位置参数
def text_info(nmae,age,gender):
    print(f"{nmae}{age}{gender}")

text_info("sax",12,23)

#关键字参数,注明的关键字参数位置可以混用
text_info("we",gender=13,age=23)

#缺省参数（设置默认值），设置默认值的项必须在最后
def text_info_1(nmae,age,gender = "男"):
    print(f"{nmae}{age}{gender}")

text_info_1("we",23)
text_info_1("we",23,gender="女")


# 不定长(数据元素个数不限) - 位置不定长, *号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是:{args}")

user_info(1, 2, 3, '小明', '男孩')

# 不定长 - 关键字不定长,作为字典存在， **号（传入的必须是key=value）
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是:{kwargs}")
user_info(name='小王', age=11, gender='男孩')

#函数作为参数传递
def sum(a,b):
    return a + b

def double(sum):#函数作为参数传递,传输的是代码逻辑
    c = sum(1,3)
    #函数调用
    print(c)

double(sum)

#匿名函数
#lambda 参数:函数体（一行代码），只能临时用一次
def double(sum):#函数作为参数传递,传输的是代码逻辑,即匿名函数定义的逻辑
    c = sum(1,3)
    #函数调用
    print(c)

double(lambda x,y:x +y)

