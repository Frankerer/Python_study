#for循环（无循环条件，无法无限循环）
#只能处理字符串
name = "Hello"
time = 0
time0 = 0
for x in name:
    #x是临时变量，在for循环里面使用
    if x == "l":
        time0  += 1
    print(x,end='')
    time += 1
print(time)
print(time0)

#range
range(5)
#0 1 2 3 4
range(2,5)
#2 3 4 (不包含5)
range(2,8,2)
#2 4 6 (不包含8，步长为2)

for x in range(2,8,2):
    print("x")

#表白
i = 1
for i in range(1,101):
    print(f"今天是第{i}天是表白")
    for j in range(1,11):
        print(f"第{j}花",end='')
print("成功")

#九九乘法表
for i in range(1,10):
    for j in range(1,i +1):
        print(f"{j} * {i} = {j * i}\t",end='')
    print()

#continue 跳过其所在循环的当此执行，转到所在循环的下一次循环
for i in range(1,6):
    for j in range(1,i):
        if j == i - 2:
            continue
        print(f"{j}")

#break 结束其所在循环的所有执行。
#111222333111222333111222333
for i in range(1,3):
    print("111",end='')
    for j in range(1,3):
        print("222",end='')
        break
    print("333",end='')

#发工资
sum = 10000
for x in range(1,21):
    import random
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{x},绩效{num},无工资，下一位")
        continue
    else:
        sum -= 1000
        print(f"向员工{x}发工资1000元，余额为{sum}元")
        if sum <= 0:
            print("工资发完")
            break