"""
演示Python的模块导入
"""
#[from 模块名] import [模块|类|变量|函数|*]  [as 别名]

#使用import导入time模块使用sleep功能（函数）
import time     # 导入Python内置的time模块（time.py这个代码文件）

import Day05_2_text02

print("你好")
time.sleep(5)   # 通过. 就可以使用模块内部的全部功能（类、函数、变量）
print("我好")

#使用from导入time的sleep功能（函数）
from time import sleep
print("你好")
sleep(5)
print("我好")

#使用 * 导入time模块的全部功能
from time import *      # *表示全部的意思
print("你好")
sleep(5)
print("我好")

#使用as给特定功能加上别名
import time as t
print("你好")
t.sleep(5)
print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")

#自定义模块

from  Day05_2_text01 import text01

from Day05_2_text02 import text01

#调用模块，重复函数名，后置覆盖前者
text01(3,1)

#__main__测试
from  Day05_2_text01 import text
from  Day05_2_text01 import text01

#__all__测试（只于*相关系）
from Day05_2_text02 import *
text(2,1)
#不可用text01(2,4)，因为all定义的列表里面没有text01功能

#自定义包的使用
# from Day5_2_package.text01 import text01
# from Day5_2_package.text02 import text02
from Day5_2_package import *
text01.text01()
#不可用text02.text02()，因为all定义的列表里面没有text01模块

#安装第三方包
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

#案例联系
from Day05_2_my_utils import str_util
str_util.str_reverse("qweqweqweqwe")
str_util.substr("qwe qwe qwe qwe","w"," ")

from Day05_2_my_utils import file_util
file_util.append_to_file("D:\software\pycharm\ text2.txt","sdvsd")
file_util.prinf_file_info("D:\software\pycharm\ text2.txt")



