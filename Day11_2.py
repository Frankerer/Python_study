"""
单例模式
"""
#就是对一个类，只获取其唯一的对象，持续的复用它

from Day11_2_1 import instance_1

s1 = instance_1
s2 = instance_1

print(f"{s1}")#0x000001A2B2888490
print(f"{s2}")#0x000001A2B2888490

"""
工厂模式
"""

#工厂类
class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "s":
            return Student()
        else:
            return Teacher()

factory = Factory()

#由原生类创造的对象
#worker0 = Worker()
#由工厂模式创造的类
worker = factory.get_person("w")

# #当大批量数据类修改时
# 原生类需要每一个worker[] = Worker2
# 工厂模式需要只进行一次工厂类内部的修改是
# if p_type == "w":
#    return Worker2()

stu = factory.get_person("s")
teacher = factory.get_person("t")