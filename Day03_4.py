"""
集合
集合是无序的，集合没有下标，没有重复元素
"""

my_set = {"my",12,True,"my",12,True,"my",12,True}
#定义空集合
my_set_empty = set()

print(f"my_set 的内容是{my_set}")
print(f"my_set 的类型是{type(my_set)}")
print(f"my_set_empty 的内容是{my_set_empty}")
print(f"my_set_empty 的类型是{type(my_set_empty)}")

#添加新元素
my_set.add("you")
print(f"my_set 的内容是{my_set}")

#移除元素
my_set.remove(12)
print(f"my_set 的内容是{my_set}")

#随机取出一个元素
fin = my_set.pop()
print(f"my_set 的取出内容是{fin}")

#清除集合
my_set.clear()
print(f"my_set 的内容是{my_set}")

#以集合1位基准，取出集合1有的，集合2没有的
set1 = {1,2,3}
set2 = {1,5,7}
set3 = set1.difference(set2)
print(f"set1的内容是{set1}")
print(f"set2的内容是{set2}")
print(f"set3的内容是{set3}")

#以集合1位基准，在集合1中删除和集合2相同的元素
set4 = set1.difference_update(set2)
print(f"set4的内容是{set4}")

#合并两个集合(合并后没有重复元素)
set5 = set1.union(set2)

#统计集合内元素个数
num = len(set5)

#遍历集合
for x in set5:
    print(x)

my_list = ['aa','bb''aa','bb','cc','dd','cc','dd','ee']
my_set = set()
for x in my_list:
    print(my_list)
    my_set.add(x)

print(my_set)
