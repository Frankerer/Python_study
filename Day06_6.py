#
# #准备列表
# my_list = [["a",33],["b",55],["c",11]]
#
# #匿名函数lambda排序
# my_list.sort(key = lambda element:element[1],reverse=True)
# print(my_list)
#
# #带名函数排序
# def choose_sort_key(element):
#     return  element[1]
#
# my_list.sort(key=choose_sort_key,reverse=True)0
# print(my_list)
#
# #根据某属性排序

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

#排序结果为列表
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
print(f"字典对象的keys排序结果：{sorted(my_dict.keys())}")
print(f"字典对象的values排序结果：{sorted(my_dict.values())}")
