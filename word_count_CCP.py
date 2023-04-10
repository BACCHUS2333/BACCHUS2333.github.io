import pandas as pd
import numpy as np
import random as rd

import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.globals import ThemeType, ToolboxOpts, TitleOpts

deve = [186,212,212,218]
social = [91,150,147,116]
China = [67,94,169,124]
people = [43,84,157,134]
econ = [49,64,59,42]
reform = [29,13,9,10]
word = ['发展','社会主义','中国','人民','经济','改革开放']
c = (
Line(init_opts = opts.InitOpts(theme = ThemeType.CHALK))
.add_xaxis(['17th','18th','19th','20th'])
.extend_axis(yaxis=opts.AxisOpts(type_ = "value",position="right",))
.add_yaxis(word[0], deve)
.add_yaxis(word[1],social)
.add_yaxis(word[2],China)
.add_yaxis(word[3], people)
.add_yaxis(word[4], econ)
.add_yaxis(word[5],reform)

)

#c.render("Line.html")

b = (
    Bar()
    .add_xaxis(['17th','18th','19th','20th'])
    .add_yaxis(series_name='总词数',y_axis=[1446,2074,3071,3123],yaxis_index=1)
    .set_series_opts(itemstyle_opts=opts.ItemStyleOpts(opacity=0.7))
    
)

c.overlap(b)
c.render("chart2.html")