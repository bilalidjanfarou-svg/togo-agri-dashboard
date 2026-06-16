# test.py
import plotly.express as px
print("start")
fig = px.bar(x=["a", "b"], y=[1, 2])
fig.write_html("graphs/test.html")
print("done")