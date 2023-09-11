def text(a, b):
    num = a + b
    print(f"两数之和为{num}")


def text01(a, b):
    num = a * b
    print(f"两数之积为{num}")

text01(2,3)

#在被其他文件import调用时，if语句不会成立
#但在本文件使用是if语句成立，函数可执行
if __name__ == '__main__':
    text(1,2)