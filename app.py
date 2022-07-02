# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
DIRECTORY='/data/'
FILE='pink_morsel_sales.csv'
file_path = os.getcwd() + DIRECTORY + FILE
df = pd.read_csv(file_path)

fig = px.line(df, x = 'date', y = 'sales', color='region', title = "Pink Morsel Sales Over Time")

app.layout = html.Div(
    className="app-header",
    children=[
    html.H1(children='Pink Morsel Sales', className="app-header-title"),

    dcc.Graph(
        id='pink morsel sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)