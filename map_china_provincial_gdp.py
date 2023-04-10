from typing import List

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line

import pandas as pd
import numpy as np

t1 = Timeline()
path = "E:\\python当学会\\homework1_visualization\\GDP.xlsx"
rawdata = pd.read_excel(path,header=0)
prov = list(rawdata['GDP'])



def paint_map(year,prov):

    #creat data for specific year
    indices = list(rawdata[year])
    data = []
    for i in range(31):
        data.append([prov[i],indices[i]])    
    min_data, max_data = (
            min([int(d[1]) for d in data]),
            max([int(d[1]) for d in data]),
        )
    print((min_data,max_data))
    #map it out
    map_gdp = (
            Map()
            .add(
                series_name="",
                data_pair=data,
                label_opts=opts.LabelOpts(is_show=False),
                is_map_symbol_show=False,
                itemstyle_opts={
                    "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                    "emphasis": {
                        "label": {"show": Timeline},
                        "areaColor": "rgba(255,255,255, 0.5)",
                    },
                },
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="中国各省GDP",
                    subtitle="GDP单位:亿元",
                    pos_left="center",
                    pos_top="top",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=25, color="rgba(0,0,0, 0.9)"
                    ),
                ),
                tooltip_opts=opts.TooltipOpts(
                    is_show=True,
                    
                    ),
                visualmap_opts=opts.VisualMapOpts(
                    is_calculable=True,
                    dimension=0,
                    pos_left="10",
                    pos_top="center",
                    range_text=["High", "Low"],
                    range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=min_data,
                    max_=max_data,
                ),
                )
        
    )

    return map_gdp
#using the function in three years
map2020 = paint_map(2020,prov)
map2019 = paint_map(2019,prov)
map2018 = paint_map(2018,prov)

#add graphs to the timeline
t1.add(map2018,"{} year regionally".format(2018))
t1.add(map2019,"{} year regionally".format(2019))
t1.add(map2020,"{} year regionally".format(2020))
#t1.add(map_chart2020,"{}year regional".format(2020))


t1.render("chart.html")
        
    