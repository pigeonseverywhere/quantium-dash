# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px
import os
from dash import Dash, html, dcc, Output, Input

external_scripts = [{
    'src': 'https://kit.fontawesome.com/a5bb4f370c.js',
    'crossorigin': "anonymous"
}]

app = Dash(__name__,
           external_scripts=external_scripts)
DIRECTORY = '/data/'
FILE = 'pink_morsel_sales.csv'
file_path = os.getcwd() + DIRECTORY + FILE

app.layout = html.Div(
    children=[
        html.Ul(
                children=[html.A( id='app-header-title', children='Pink Morsel Sales'),
                           html.I(className='fa-solid fa-chart-line fa-2xl')]),
        html.Label('Select region:', style={'padding-left': 80, 'margin-bottom': 0, 'padding-bottom': 0}),
        dcc.RadioItems(id='region-radio',
                       options=['north','east','south', 'west', 'all'],
                       value='north',
                       inline=True
                 ),
        dcc.Graph( id='graph' )
])


@app.callback(
    Output('graph', 'figure'),
    Input('region-radio', 'value')
)
def update_line_chart(region):
    df = pd.read_csv(file_path)
    if region == 'all':
        figure = px.line(df, x='date', y='sales', color='region', title="Pink Morsel Sales Over Time")
    else:
        mask = (df['region'] == region)
        figure = px.line(df[mask], x = 'date', y = 'sales', color='region', title = "Pink Morsel Sales Over Time")
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)