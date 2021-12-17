import plotly.graph_objects as go


# CREAMOS UNA FIGURA
figura = go.Figure(data=go.Bar(x=[1, 2, 3], y=[2, 4, 6]))
figura.show()
# figura.write_html("graficos.html", auto_open=True)
