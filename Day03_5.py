"""
字典
{key:value,key1:value}
key不可以重复
key:value可以是任何数据类型，key不可以是字典,不可以使用下标索引，要通过key来找
"""

#定义字典
my_dict = {"wang":11,"zhang":22,"li":33}
#定义空字典
my_dict0 = {}
my_dict1 = dict()
print(f"字典内容是{my_dict}{my_dict0}{my_dict1},类型是{type(my_dict1)}")

#定义重复字典
my_dict = {"wang":11,"zhang":22,"zhang":11,"li":33}#重复着覆盖

#由key找value
num = my_dict["wang"]

#定义定义嵌套字典
stu_score_dict = {
    "wang":{
        "aa":11,
        "bb":22,
        "cc":33
    },
    "zhang":{
        "aa":22,
        "bb":33,
        "cc":44
    },
    "li":{
        "aa":33,
        "bb":44,
        "cc":55
    }
}
print(stu_score_dict)

#查询嵌套字典的信息
num0 = stu_score_dict["wang"]["aa"]

#新增字典元素
stu_score_dict["zhao"] = {"aa":44,"bb":55,"cc":66}
print(stu_score_dict)

#更新字典元素
stu_score_dict["zhao"] = {"aa":11,"bb":22,"cc":33}
print(stu_score_dict)

#删除（取出）字典元素
fin = stu_score_dict.pop("zhao")
print(stu_score_dict)
print(fin)

#获取全部的key
keys = stu_score_dict.keys()
print(f"keys为{keys},类型为{type(keys)}")
#keys为dict_keys(['wang', 'zhang', 'li']),类型为<class 'dict_keys'>

#遍历
for x in stu_score_dict.keys():
    print(f"value为{stu_score_dict[x]}")
    print(f"key为{x}")

#统计元素个数
num1 = len(stu_score_dict)
print(num1)

#清空字典
stu_score_dict.clear()

entire_person = {
    "wang":{
        "部门":"科技",
        "工资":3000,
        "级别":1
    } ,
    "li":{
        "部门":"市场",
        "工资":5000,
        "级别":2
    },
    "lin":{
        "部门":"市场",
        "工资":7000,
        "级别":3
    },
    "zhang":{
        "部门":"科技",
        "工资":4000,
        "级别":1
    },
    "liu":{
        "部门":"市场",
        "工资":6000,
        "级别":2
    },
}

print("员工信息 如下")

print(f"初始{entire_person}")
for x in entire_person:
    if entire_person[f"{x}"]["级别"] == 1:
        entire_person[f"{x}"]["级别"] += 1
        entire_person[f"{x}"]["级别"] += 1000


print(f"更改后{entire_person}")




