from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter, Bar, Pie
from pyecharts.faker import Faker
import random as rd


#creating the simulation data
def digit(number,n=4):
    number = float('{:.4f}'.format(number))
    return number
stockA, stockB = [],[]
incA, incB = [],[]
for i in range(7):
    stockA.append(rd.randrange(100,120))
    
   
    stockB.append(digit(rd.random()*100))
    if i ==0:
        continue
    else:
        incA.append(digit((stockA[i]-stockA[i-1])/stockA[i]*100))
        incB.append(digit((stockB[i]-stockB[i-1])/stockA[i]*100))

#create a scatter graph based on the increase of stock price

time = ["t"+str(i) for i in range(7)]
print(stockA,stockB,incA,incB)
scatter = (
    Scatter()
    .add_xaxis(time)
    .add_yaxis("stock A", stockA)
    .add_yaxis("stock B", stockB)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="stock price",pos_bottom="2%",pos_left="70%"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
    
)

#create a bar graph based on the increase of stock price


bar = (
    Bar()
    .add_xaxis(time[1:])
    .add_yaxis("stockA", incA)
    .add_yaxis("stockB", incB)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="increase of stock price", pos_bottom="2%",pos_right="60%"),
        legend_opts=opts.LegendOpts(pos_right="20%"),
    )
)

grid = (
    Grid()
    .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
    .add(bar, grid_opts=opts.GridOpts(pos_right="55%"))        
    
    .render("grid_horizontal.html")
)