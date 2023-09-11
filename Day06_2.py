
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts


map = Map()


data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
map.add("地图",data,"china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,#显示颜色
        is_piecewise=True,#手动校准颜色范围
        pieces=[
            {"min":1,"max":100,"label":"1~100人","color":"#CCFfFF"},
            {"min": 100, "max": 300, "label": "100-300", "color": "#FF6666"},
            {"min": 300, "max": 500, "label": "300-500", "color": "#990033"}
        ]

    )
)

map.render()