
#简单柱状图


from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar2 = Bar()
bar3 = Bar()

#定义X轴，Y轴:为了明确X,Y是谁，后调用,X，Y是个列表
bar1.add_xaxis(["中国","美国","英国"])
#数字标识放右边
bar1.add_yaxis("GDP",[30,10,20],label_opts=LabelOpts(position="right"))
#反转X,Y轴
bar1.reversal_axis()

bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[40,20,25],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[60,30,45],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

#实例化时间线
timeline = Timeline({"theme":ThemeType.LIGHT})

#建立时间节点图表
timeline.add(bar1,"2021年GDP")
timeline.add(bar2,"2022年GDP")
timeline.add(bar3,"2023年GDP")

#设置自动循环播放
timeline.add_schema(
    play_interval=1000,#自动播放的时间间隔，单位毫秒
    is_timeline_show= True,#是否在自动播放的时候，显示时间线
    is_auto_play=True,#是否自动播放
    is_loop_play=True#是否循环自动播放
)

# 绘图是用时间线对象绘图，而不是bar对象了
timeline.render("基础时间线柱状图.html")
