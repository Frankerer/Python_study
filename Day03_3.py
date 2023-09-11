#切片
my_list = [0,1,2,3,4,5,6]
fin = my_list[1:4]
print(fin)
#步长默认为1，从下标1到下标4 - 1 结束，[1, 2, 3]
fin_0 = my_list[3:1:-1]
# [3,2]

my_tuple = (0,1,2,3,4,5,6)
fin0 = my_tuple[:]
fin0_1 = my_tuple[::-2]
#(6,4,2,0)
#不写默认从头取到尾，步长为1

my_str = "0123456"
fin1 = my_str[::2]
#步长为2


my_str0 = "0123456"
fin2 = my_str[::-1]
#步长为2

#取出hello
my_str = "ack,ollehq,zcm"
#直接倒叙取出{从第4位取到第9位，倒叙输出}
FIN = my_str[9:4:-1]
#倒叙，切片取出
FIN01 = my_str[::-1][5:11]
#切片取出，倒叙
FIN02 = my_str[4:9][::-1]
#按逗号切片得到三个元素的列表，取出第2个元素，取代不需要项，倒叙输出
FIN03 = my_str.split(",")[1].replace("q","")[::-1]



