#字符串也是容器
#下标索引取值

string_1 = "qwdwcd caca caw  "
v1 = string_1[0]
print(len(string_1))
v2 = string_1[-17]
print(f"{v1}{v2}")

#统计w出现的次数
time = string_1.count("w")
print(time)

#下标索引
num = string_1.index('cd')
print(num)

#用位置2的值覆盖位置1，来得到一个新字符串
string_2 = string_1.replace("ca","zz")
print(string_1)
print(string_2)

#切割字符串，存储在列表中
string_3 = string_1.split(" ")
print(string_1)
print(f"{string_3},{type(string_3)}")

#去除前后字符串
string_4 = string_1.strip()
string_5 = string_1.strip("qw")
print(string_4)
print(string_5)

