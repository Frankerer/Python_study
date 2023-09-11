"""
json数据格式
本质是一个字符串，内容是一个单独的字典或者一个内部元素都是字典的列表
"""
import  json

#字典转json
dict_str = {"name":"wang","age": 12,"gender" : "男"}
json_dict_str = json.dumps(dict_str,ensure_ascii=False)
print(f"格式为{type(json_dict_str)},内容是{json_dict_str}")

#内部元素都是字典的列表转json
list_str = [{"name":"wang","age": 12,"gender" : "男"},{"name":"liu","age": 16,"gender" : "男"},{"name":"zhang","age": 12,"gender" : "女"}]
json_list_str = json.dumps(list_str,ensure_ascii=False)
print(f"格式为{type(json_list_str)},内容是{json_list_str}")

#json转字典
s0 = '{"name":"wang","age": 12,"gender" : "男"}'
dict_json_str = json.loads(s0)
print(f"格式为{type(dict_json_str)},内容是{dict_json_str}")

# #jsonz转内部元素都是字典的列表
s = '[{"name":"wang","age": 12,"gender" : "男"},{"name":"liu","age": 16,"gender" : "男"},{"name":"zhang","age": 12,"gender" : "女"}]'
list_json_str = json.loads(s)
print(f"格式为{type(list_json_str)},内容是{list_json_str}")


