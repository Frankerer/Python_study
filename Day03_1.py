#元组，数据可读不可修改,元组内必须有，号，有索引下标。

#定义
('ac',)
(1,"qwd",True)
YuanZu = (2,"ac",False,None)
print(YuanZu)

#空元组
YuanZu0 = ()
YuanZu1 = tuple()

#单个元组
YuanZu1_1 = (12,)

#嵌套元组
YuanZu2 = ((1,2,3),(4,5,6))
print(YuanZu2[0][1])

#查找元组内元素
YuanZu3 = ((123,234,345),[321,432,543])
num = YuanZu3.index((123,234,345))
print(f"123的下标是{num}")

#修改元组内容中的list内元素
YuanZu3[1][1] = 222
print(YuanZu3)
#((123,234,345),[321,222,543])

#统计某元素个数,总元素数
t9 = (12,12,23,1,34,1)
num0 = t9.count(1)
print(f"1的个数为{num0}")
print(f"总元素数为{len(t9)}")

def tuple_while(x):
    i = 0
    while i <len(x):
        print(x[i])
        i += 1
    print(f"while遍历有数据{i}个")
    return  None

def tuple_for(x):
    i = 0
    for y in x:
        print(y)
        i += 1
    print(f"for遍历有数据{i}个")
    return None

tuple_while((12,12,13))
tuple_for((12,12,13))

YuanZu4 = ("wang",11,['back','music'])
print(YuanZu4.index(11))
print(YuanZu4[0])
del YuanZu4[2][1]
print(YuanZu4)
YuanZu4[2].append("coding")
print(YuanZu4)

