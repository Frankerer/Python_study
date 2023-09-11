"""
捕获异常
"""

"""
try:
    某异常
except (异常名称1，异常名称2，...):
    对异常的处理
else:
    没有异常时会出现的情况
finally:
    无论是否异常都会执行的代码
"""


#知道异常，捕获异常，重写异常
try:
    print(name)
except:
    print("姓名异常")

#捕获指定异常
try:
    f = open("D:/software/pycharm/code/text_A.txt","r",encoding="UTF-8")
except FileNotFoundError as e:
    print("找不到该文件")
    print(e)

#捕获多个异常
try:
    1/0
except(NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常错误")

#捕获所有异常
try:
    f = open("D:/123.txt","r")
except Exception as a:
    print("出现异常")
else:
    print("无异常")
finally:#无论是否异常都会执行的代码
    f.close()

#异常的传递型
def func01():
    print("func01启动")
    num = 1/0
    print("func01结束")

def func02():
    print("func02启动")
    func01()
    print("functi02结束")

def main():
    try:
        func02()
    except Exception as e:
        print(f"出现异常，类型为{e}")

main()