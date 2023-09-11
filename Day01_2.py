num = 1
sum = 0
while num <= 100:
    sum +=num
    num +=1
print(f"{sum}")

#猜数
import random
num = random.randint(1,10)
guess_num = 0
time = 0
while  guess_num != num:
    if guess_num >= num:
        print("猜错了，,偏大，请重新输入")
    else:
        print("猜错了，偏小，请重新输入")
    guess_num = int(input("输入数字"))
    time +=1
print(f"次数为{time},猜对")

#送花
i = 0
while i < 10:
    print(f"day{i+1}")
    j = 0
    while j < 10:
        print("花")
        j += 1
    i += 1
    print("Love")
print("succssed")

#九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        if j == i:
            print(f"{j}*{i} = {i * j}\t")
        else:
            print(f"{j}*{i} = {i * j}\t", end='')
        j += 1
    i +=1
