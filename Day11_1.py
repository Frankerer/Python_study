"""
闭包
定义双层嵌套函数，内层函数可以访问外部函数的变量，就不用单独设立全局变量，承担被外部篡改的风险，因为，嵌套的函数中，外部函数作用域是封闭的。
"""

def action_value(sum = 0):
    def ATM(num,deposit = True):
        nonlocal sum#在闭包函数中（内部函数中）修改外部函数的值
        if deposit:
            sum +=num
            print(f"存款+{num},余额{sum}")
        else:
            sum -= num
            print(f"取款-{num},余额{sum}")

    return ATM

atm = action_value()

atm(12)
atm(15,deposit=False)

"""
装饰器
"""
#使用创建一个闭包函数。在闭包函数内调用目标函数，可以达到不改动目标函数，增加额外功能

def outer(func):
    def inner():
        print("开始")
        func()
        print("结束")
    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中——————")
    time.sleep(random.randint(1,5))

sleep()