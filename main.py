import pandas
import plotly.express as px

data = pandas.read_csv("data.csv")
chart = px.scatter(data, x="date", y="cases", color="country")
chart.show()
