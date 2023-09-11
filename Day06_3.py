import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

#读取文件
f = open("D:\software\pycharm\code\数据\疫情.txt","r",encoding="UTF-8")

#获取数据
date = f.read()

#关闭文件
f.close()

#将JSON转为字典格式
date_dict = json.loads(date)

#定位初始节点
province = date_dict["areaTree"][0]["children"]

#更正省份名称
for x in range(0,34):
    str1 = str(province[x]["name"])
    province[x]["name"] = str1 + "省"

#备用列表，装入（X,Y）的元组数据
date_list =[]

#将（X,Y）元组值装入列表，:为了明确X,Y是谁，组成元组后调用
for province_date in province:
    X = province_date["name"]
    Y = province_date["total"]["confirm"]
    date_list.append((X,Y))

# print(date_list)

#初始化地图实例
map = Map()

#注入数据
map.add("地图",date_list,"china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,#显示颜色
        is_piecewise=True,#手动校准颜色范围
        pieces=[
            {"min":1,"max":1000,"label":"1~100人","color":"#CCFfFF"},
            {"min": 1000, "max": 5000, "label": "100-300", "color": "#FF6666"},
            {"min": 5000, "max": 100000, "label": "300-500", "color": "#990033"}
        ]

    )
)

map.render()