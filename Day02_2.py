def text01(num):
    print(f"欢迎")
    if num < 38:
        print(f"测试——，体温{num},进入")
    else:
        print(f"测试——，体温{num},出去")
text01(int(input("请输入数字")))

#有返回值的相加操作
#遇到return就结束函数
def add(a,b):
    """
    add相加操作
    :param a 加数:
    :param b 加数:
    :return 返回和:
    """
    sum_add = a + b
    return  sum_add
    #print("花")
num = add(2,4)
print(num)

#无返回值（None）的函数
def say_hi():
    print("hi")
    #return None加不加效果一样
hi = say_hi()
print(f"返回东西{hi}")
print(f"返回类型{type(hi)}")

#检查是否成年
#None == flase
def check_age(a):
     if a < 18:
         return "fail"
     else:
         return None
fin = check_age(19)
if not fin:
    print("okk")

"""
演示嵌套调用函数
"""
# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a，并在内部调用func_b
def func_a():
    print("---1---")

    # 嵌套调用func_b
    func_b()

    print("---3---")
# 调用函数func_a
func_a()

"""
局部变量与全局变量
局部变量只能在所在函数内体定义和使用
全局变量可以在函数内和函数外使用
"""

def text001():
    num001 = 100
    print(num001)
text001()
#print(num001)


num002 = 100
def text002():
    #num002 =200
    #非使用全局变量num002,只是内部定义局部变量

    #global 关键字声明全局变量
    global num002
    #更改全局变量
    num002 += 1
    print(num002 +1)
text002()
print(num002)


"""
ATM
"""

sum = 10000

def step1(x):
    print("----------余额----------")
    print(f"余额为{sum}")

def step2(x):
    global sum
    print("----------存款----------")
    sum += float(input("输入存款金额"))
    print(f"存款后余额为{sum}")

def step3(x):
    global sum
    print("----------取款----------")
    sum -= float(input("输入取款金额"))
    print(f"取款后余额为{sum}")


def main_enter(x):
    print("----------主菜单----------")
    print(f"{x},你好，ATM,请操作")
    print("查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
    num = int(input("输入选择"))
    global name
    if num == 1:
        step1(num)
        main_enter(name)
    elif num == 2:
        step2(num)
        main_enter(name)
    elif num == 3:
        step3(num)
        main_enter(name)
    else :
        print("欢迎下次使用")
        return  None

name = input("请输入名字")
main_enter(name)


