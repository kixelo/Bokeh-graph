#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bokeh.plotting import figure, output_file, show
import pandas
from bokeh.models import HoverTool, ColumnDataSource

#df=pandas.read_csv("https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410912000&period2=1639958400&interval=1d&events=history&includeAdjustedClose=true",parse_dates=["Date"])
df=pandas.read_csv("coin_Bitcoin.csv",parse_dates=["Date"])

df["Date_string"]=df["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")

# create a ColumnDataSource by passing the dict
source = ColumnDataSource(df)

p=figure(width=500,height=250,sizing_mode="stretch_both",x_axis_type="datetime")

p.title.text = "Bitcoin USD (BTC-USD) High Price History"
p.title.text_color = "Black"
p.title.text_font = "times"
p.title.text_font_style = "bold"
p.title.text_font_size = "20pt"
p
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Price USD"

hover=HoverTool(
    tooltips=[
        ("Date", "@Date_string"), #( 'Date',   '@Date{%F}' - alternative
        ("Price", "$@High{%.2f}"),
    ],
    
formatters={
    #'@Date'  : 'datetime', # use 'datetime' formatter for '@Date' field
    "@High" : "printf", # use 'printf' formatter for '@High' field
    
},

# display a tooltip whenever the cursor is vertically in line with a glyph
mode="vline"
)

p.add_tools(hover)

p.line(x="Date", y="High",color="Orange",alpha=0.5,line_width=1.5,source=source)

output_file("Bitcoin_price_history.html")
show(p)

