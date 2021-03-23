import pandas as pd 
import plotly.express as pe

df = pd.read_csv("Covid.csv")

fig=pe.scatter(df,x='date', y='cases', color='country', size_max=60)
fig.show()