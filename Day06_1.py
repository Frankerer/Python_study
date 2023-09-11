import json
from pyecharts.charts import Line
from pyecharts.options import LabelOpts
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts



#打开数据
f_us = open("D:\software\pycharm\code\数据\美国.txt","r",encoding="UTF-8")
f_jp = open("D:\software\pycharm\code\数据\日本.txt","r",encoding="UTF-8")
f_in = open("D:\software\pycharm\code\数据\印度.txt","r",encoding="UTF-8")

#读取数据
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

#掐头去尾
us_data = us_data.replace("jsonp_1629344292311_69436(","")
us_data = us_data[:-2]
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
jp_data = jp_data[:-2]
in_data = in_data.replace("jsonp_1629350745930_63180(","")
in_data = in_data[:-2]

#Json格式转为字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
#print(f"类型是{type(us_dict)},内容是{us_dict}")

#定义X轴，Y轴:为了明确X,Y是谁，后调用,X，Y是个列表，
us_X_data = us_dict["data"][0]["trend"]["updateDate"][:314]
# print(us_X_data)
jp_X_data = jp_dict["data"][0]["trend"]["updateDate"][:314]
in_X_data = in_dict["data"][0]["trend"]["updateDate"][:314]
us_Y_data = us_dict["data"][0]["trend"]["list"][0]["data"][:314]
# print(us_Y_data)
jp_Y_data = jp_dict["data"][0]["trend"]["list"][0]["data"][:314]
in_Y_data = in_dict["data"][0]["trend"]["list"][0]["data"][:314]

# print(us_X_data)
# print(us_Y_data)


#定义对象
line = Line()


line.add_xaxis(us_X_data)#三者皆是相同的日期数据
line.add_yaxis("us_确诊",us_Y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("jp_确诊",jp_Y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("in_确诊",in_Y_data, label_opts=LabelOpts(is_show=False))

# 设置全局配置项set_global_opts来设置,
line.set_global_opts(
    title_opts=TitleOpts(title="确诊趋势", pos_left="center", pos_bottom="1%"),#标题配置项
    legend_opts=LegendOpts(is_show=True),#图例配置项
    toolbox_opts=ToolboxOpts(is_show=True),#工具箱配置项
    visualmap_opts=VisualMapOpts(is_show=True, pos_left="right", pos_bottom="1%"),#视觉映射配置项
)

#生成折线图
line.render()

#关闭文件
f_us.close()
f_jp.close()
f_in.close()



