"""
变量的类型注解
"""
import random,json
from typing import Union

#基础类型的注解
a : int = 10
b : float = 54.102
c : bool = True
d : str = "abc"

#类对象注解
class Student:
    ID : int
    contry :str

stu : Student = Student()

#基础容器类型注解
my_list : list = [1,2,3]
my_tuple : tuple = (1,2,3)
my_set : set = {1,2,3}
my_dict : dict = {"name":"姓名"}
my_str : str = "abc"

#容器类型详细注解
my_list : list[int]
my_tuple : tuple[int,str,bool]
my_set : set[{int,bool}]
my_dict : dict[str,int]#key需要str,value需要int

#在注释中进行类型注解
var_1 = random.randint(1,10) #type:int
data = "abc"
var_2 = json.loads('{"name":"zhang}') #type:dict

#函数方法中的类型注解
def add(a:int,b:float,data:list)->list:#返回值是list
    data = []
    data.append(a + b)
    return data

#union[仅可选用类型]的类型注解
my_list:list[Union[int,str]]

def func001(data:Union[int,bool])->Union[int,str]:
    pass

func001(True)







