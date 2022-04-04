import os
from flask_caching import Cache
import dash
from dash import dash_table, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd


# reading data
df_historical_matchups = pd.read_csv('dash_app/data/historical_matchups.csv')
#prediction_df_list = [pd.read_csv(f'frontend/assets/{x}.csv') for x in range(6)]
#summary_statistics = pd.read_csv()
example_prediction = pd.read_csv('dash_app/data/example_prediction.csv')

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG,
    ],
    # Dash throws exceptions about callbacks from components that might be not loaded yet if
    # elements like Tabs are used. These alerts are annoying so suppress them.
    suppress_callback_exceptions=True,
    title='dash_app',
)
cache = Cache(
    app.server,
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': os.path.join('/Users/alexiskaldany/school/cloud-computing-finale', 'dash-cache'),
    }
)
app.layout = html.Div(children=[html.H1(id='Header', children=['Black Mamba'], style={'textAlign': 'center'}),
                                dash_table.DataTable
                                (id='example_prediction', data=example_prediction.to_dict('records'), columns=[{"name": i, "id": i} for i in example_prediction.columns], style_cell={'textAlign': 'left', 'width': '{}%'.format(len(example_prediction.columns)),
                                                                                                                                                                                      'textOverflow': 'ellipsis',
                                                                                                                                                                                      'overflow': 'hidden'}, page_size=10, style_data={
                                    'whiteSpace': 'normal',
                                    'height': 'auto',
                                }
)
])
