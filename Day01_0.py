############################################################################
#标识符
# 规则1：内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能以数字开头
# 错误的代码示范：1_name = "张三"
# 错误的代码示范：name_! = "张三"
name_ = "张三"
_name = "张三"
name_1 = "张三"

# 规则2：大小写敏感
Itheima = "黑马程序员"
itheima = 666
print(Itheima)
print(itheima)

# 规则3：不可使用关键字
# 错误的示例，使用了关键字：class = 1
# 错误的示例，使用了关键字：def = 1

############################################################################
# """多行注释"""
"""
多行注释
"""

#单行注释

############################################################################
# 通过print语句输出各类字面量
print(666)
print(13.14)
print("黑马程序员")

"""
数据类型
"""

#常量 int float
print(type(22))
print(type(22.11))

#数字精度
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)#___11
print("数字11宽度限制1，结果是：%1d" % num1)#11(若数字设置宽度比本身小，相当于没写)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)#__11.34
print("数字11.345不限制，小数精度2，结果是：%.2f" % num2)#11.34


print(22+11)
print(22-11)
print(22*11)
print(22/11)
print(22%11)#求余
print(22//11)#取整
print(6**3)#6的3次方
#赋值运算符
num = 1 + 2 * 3
#复合赋值运算符
num += 1  #num = num + 1
print("num += 1",num)
num -= 1
print("num -= 1",num)
num *= 1
print("num *= 1",num)
num /= 1
print("num /= 1",num)
num %= 1
print("num %= 1",num)
num //= 1
print("num //= 1",num)
num **= 1
print("num **= 2",num)

#字符串常量 string
name1 = "字符型"
name2 = '字符型'
name3 = """字符型"""
name4 = "\"加入转义字符"
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))

#字符串的拼接使用+号
print("Hello"+"jia")
name5 = 123
#数字不可以直接用+号拼接
print("name1"+name1+"name5",name5)

# 通过字符型占位的形式，完成拼接
name = "程序员"
message = "IT：%s" % name
print(message)

# 通过整数和浮点数占位的形式，完成拼接
name = "智客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立于：%d，我今天的股价是：%f" % (name, setup_year, stock_price)
print(message)

# 通过f"{ 占位 }"
#   没有精度控制
print(f"{name},成立于：{setup_year}，我今天的股价是：{stock_price}")

# 表达式格式化占位
print("1 + 2 的结果是： %d " % (1 +1))
print(f"1 + 2 的结果是： %d  { 1 + 2 } ")
print("字符串类型名是：%s" % type("字符串"))

#拼接应用
A_a = "Hello"
A_b = "wang"
A_c = 11
A_d = 22.1

#多个变量占位，要用括号括起来，按顺序占入
ma = "首先"+A_a+"姓%s,年龄%d" % (A_b,A_c),A_d
print(ma)
print("首先"+A_a+"姓%s,年龄%f" % (A_b,A_d))


############################################################################
#数字类型转换
#str(),int(),float()
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)
# 将字符串转换成数字
num = int("11")
print(type(num), num)

num2 = float("11.345")
print(type(num2), num2)

# 错误示例，想要将字符串转换成数字，必须要求字符串内的内容都是数字
# num3 = int("黑马程序员")
# print(type(num3), num3)

# 整数转浮点数
float_num = float(11)
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(11.345)
print(type(int_num), int_num)

############################################################################
#变量 ————
# 定义一个变量，用来记录钱包余额
money = 50
# 通过print语句，输出变量记录的内容
print("钱包还有：", money)

# 买了一个冰淇淋，花费10元
money = money - 20
print("买了冰淇淋花费10元，还剩余：", money, "元")
############################################################################

#input()函数

print("名字")
name = input()
print("名字是%s" % name)

name = input("名字")
print("名字是%s" % name)

age = input("年龄")
#默认得到字符串型数据
int(age)
print("年龄是：", age)
print("年龄是：", type(age))

#######################################################







