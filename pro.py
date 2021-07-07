
import pandas as pd
import csv
import plotly.graph_objects as go #grouping data

df= pd.read_csv("data1.csv")
print(df.groupby("level")["attempt"].mean()) #getting data of all students and get the mean of the attempt of lvel1

fig=go.Figure(go.Scatter( #draw horizontal bar graph
    x=df.groupby("level")["attempt"].mean(), #grouping all the things (groupby)
    y=['Level 1', 'Level 2','Level 3', 'Level 4'],
    orientation='h')) #if we write h it will show horizontal and if we write v then vertical

fig.show()


