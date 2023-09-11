"""
多态
多种状态下，完成某个行为，使用不同的对象会得到不同的状态
"""
class Animal:#抽象类：作为标准
    def speak(self):#抽象方法，作为接口
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

dog = Dog()
cat = Cat()

def make_animal(animal:Animal):#以父类做定义声明
    animal.speak()#以子类做实际工作
   #同一行为，不同状态

make_animal(dog)
make_animal(cat)

