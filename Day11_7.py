#递归

import os

def rest_os():
    print(os.listdir("D:/software/pycharm/code/数据/test"))   #列出路径下的内容
    print(os.path.isdir("D:/software/pycharm/code/数据/test"))    #判断指定路径是不是文件夹
    print(os.path.exists("D:/software/pycharm/code/数据/test"))   #判断指定路径是否存在



rest_os()
file_list = []
def healal_self(Raw):
    fin_row = os.listdir(Raw)
    for raw in fin_row:
        new_Raw =Raw + "/" + raw
        if os.path.isdir(new_Raw):
            Raw01 = new_Raw
            file_list.append(Raw01)
            healal_self(Raw01)
        else:
            file_list.append(new_Raw)



healal_self("D:/software/pycharm/code/数据/test")
print(file_list)