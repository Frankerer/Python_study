from  pyecharts.charts import Bar,Timeline
from  pyecharts.options import LabelOpts,TitleOpts
from pyecharts.globals import ThemeType


f = open("D:\software\pycharm\code\数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
date_lines = f.readlines()
f.close()
date_lines.pop(0)
# print(date_lines)

#实例化时间线
timeline = Timeline({"theme":ThemeType.LIGHT})

#定义目标字典
#即进行数据处理
data_dict = {}

for line in date_lines:
    year = int(line.split(",")[0]) #获取年份
    country = line.split(",")[1] #获取国家
    gdp = float(line.split(",")[2]) #获取GDP

    #以下操作为了得到目标字典形式  {年份：[[国家，GDP],[国家，GDP],[国家，GDP]...],年份：[[国家，GDP],[国家，GDP],[国家，GDP]...]}
    #思想：如果年份已经存在（不异常），直接为该年份的value（格式为列表）添加列表元素[国家，GDP]，否则
    #如果年份已经不存在（异常），进行异常处理，建立该年份的新列表，即———》新年份：value《————， value（格式为列表），后为该年份的value添加列表元素[国家，GDP]
    try:
        #年份已经存在（不异常）
        data_dict[year].append([country,gdp])
    except KeyError:
        #年份已经不存在（异常）
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# print(data_dict)



#保证年份有序的情况下，选取前8名GDP高的
sort_year_list = sorted(data_dict.keys())

for year in sort_year_list:
    data_dict[year].sort(key=lambda element:element[1],reverse=True)
    #取出GDP前8名国家,取出的是该年份的元组元素
    year_data = data_dict[year][0:8]
    #至此得到了一幅柱状图的Y轴所需参数

    X_data = []
    Y_data = []
    #选择元组元素（X,Y）中的元素X,元素Y分别做X轴，Y轴
    for country_gdp in year_data:
        X_data.append(country_gdp[0]) #X轴添加国家
        Y_data.append(country_gdp[1]/100000000) #Y轴添加GDP

    #构建柱状图
    bar = Bar()
    X_data.reverse()
    Y_data.reverse()
    bar.add_xaxis(X_data)
    bar.add_yaxis("GDP",Y_data,label_opts=LabelOpts(position="right"))
    #反转X，Y轴
    bar.reversal_axis()

    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar,str(year))

#设置自动循环播放
timeline.add_schema(
    play_interval=1000,#自动播放的时间间隔，单位毫秒
    is_timeline_show= True,#是否在自动播放的时候，显示时间线
    is_auto_play=True,#是否自动播放
    is_loop_play=True#是否循环自动播放
)

#绘图
timeline.render("1960~2019千秋GDP前八的国家.html")