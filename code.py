import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv('main.csv')

toelf = df['TOEFL Score'].tolist()

Cof= df['SOP'].tolist()

Px = px.scatter(x = toelf, y = Cof)
Px.show()

m=0.10
c=-2.5
y=[]

for i in toelf:
    y_val = m*i+c
    y.append(y_val)

Px = px.scatter(x = toelf, y = Cof)
Px.update_layout(shapes = [dict(type='line',y0=min(y), y1=max(y), x0=min(toelf), x1 = max(toelf))])
Px.show()    

x=600
y=m*x+c
print(f'sop value of {x} is {y}')