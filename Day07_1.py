class Student:

    def dump_stu(self):
        print(f"学生{self.name}DUMP")

    def say_say(self,msg):
        print(f"学生{self.name}说{msg}")

    def __init__(self,name,gender,contry,age):#构造类对象是自动执行的
        self.name = name
        self.contry = contry
        self.gender = gender
        self.age = age
        print("构建了一个对象")

    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    def __lt__(self, other):# lt：less than 小于
        return self.age < other.age
        #返回的是True或者Flase

    def __le__(self, other):# le：less than or equal to 小于等于
        return self.age <= other.age
        #返回的是True或者Flase

    def __eq__(self, other):#eq：equal to 等于
        return self.age == other.age
        #返回的是True或者Flase


stu_1 = Student("wang","男","china", 18)#自动传入参数给__init__方法使用
# stu_1.age = 19
# print(stu_1.age)
# print(stu_1.contry)
# stu_1.dump_stu()
# stu_1.say_say("stu_1.name")

stu_2 = Student("zhang","女","china", 17)
print(stu_2.name)
print(stu_2.gender)

#可以通过魔术方法__str__,来控制类对象使用魔术方法__str__规定的return来返回结果
print(stu_1)
#Student类对象，name:wang,age:18
print(type(stu_1))
print(str(stu_1))

#可以通过魔术方法__lt__,来控制类对象之间的比较，使用魔术方法__lt__所规定的：对象中的某元素进行比较，来返回True OR Flase
print(stu_1 < stu_2)#18>17,结果是Flase

#可以通过魔术方法__le__,来控制类对象之间的比较，使用魔术方法__le__所规定的：对象中的某元素进行比较，来返回True OR Flase
print(stu_1 <= stu_2)#18>17,结果是Flase
print(stu_1 >= stu_2)#18>17,结果是True

# #可以通过魔术方法__eq__,来控制类对象之间的比较，使用魔术方法__eq__所规定的：对象中的某元素进行比较，来返回True OR Flase
print(stu_1 == stu_2)#结果是Flase
print(stu_1 != stu_2)#结果是True


#类内成员前加__就是私有
class Phone:
    ID = None
    producer = None
    face_id = "1001"
    __root = None
    __is_5g_enable = bool

    #类内方法可以使用类内私有属性
    def open(self):
        print(f"{self.ID}已经打开")
        print(f"{self.__root}已经打开")

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭")

    def call_by_5g(self):
        self.__check_5g()
        print("通话中")

    def __close(self):
        print(f"{self.ID}已经关闭")
        print(f"{self.__root}已经关闭")

phone = Phone()
phone.ID = 123
phone.call_by_5g()

class Phone00:
    face_id = "0000"

#单继承
class Phone01(Phone):
    face_id = "1001"
    def call_by_6g(self):
        print("这是6g")

phone01 = Phone01()
print(phone01.ID)
print(phone01.face_id)
phone01.call_by_6g()
phone01.call_by_5g()

#多继承
class Phone02(Phone,Phone00):
    force_id = "2002"
    face_id = "2002"
    def call_by_7g(self):
        print("这是7g")

phone02 = Phone02()
print(phone01.ID)
print(phone01.face_id)
print(phone02.force_id)
phone02.call_by_7g()
phone01.call_by_6g()
phone01.call_by_5g()

#不添加额外类内容
class Phone03(Phone,Phone00):
    pass

class Phone04(Phone,Phone00):
    face_id = "3003"#复写成员属性

    def open(self):#复写成员方法
        print(f"复写{self.ID}已经打开")

        #选定使用父类的成员属性和成员方法
        #方法一
        print(f"使用父类的成员属性{Phone.face_id}")
        Phone.open(self)#需要加self
        #方法二
        print(f"使用父类的成员属性{super().face_id}")
        super().open()  # 不需要加self

        #print(f"复写{self.__root}已经打开")#不可更改父类的私有属性和方法

phone00 = Phone00()

#当重复继承同样成员变量时，会优先继承较早出现的类的成员变量
phone3 = Phone03()
print(phone3.face_id)
#继承的是Phone的face_id = “1001"

phone4 = Phone04()
print(phone.face_id)
print(phone.open())
print(phone00.face_id)
print(phone4.face_id)
phone4.open()



