import dash
from dash import dcc
from dash import html
from dash import Dash, dash_table, html, dcc
import dash_bootstrap_components as dbc
#import boto3
import pandas as pd


# reading data
df_historical_matchups = pd.read_csv('data/historical_matchups.csv')
#prediction_df_list = [pd.read_csv(f'frontend/assets/{x}.csv') for x in range(6)]
summary_statistics = pd.read_csv('data/tr_data_hub_3-30-22.csv')
example_prediction = pd.read_csv('data/example_prediction.csv')
# functions
# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])

# #table_summary = [html.H1(id='Header', children=['Black Mamba','Summary Statistics'], style={'textAlign': 'center'}),
#                  dash_table.DataTable
#                  (id='summary_statistics',
#                   data=summary_statistics.to_dict('records'),
#                   columns=[{"name": i, "id": i}
#                            for i in example_prediction.columns],
#                   style_cell={'textAlign': 'left', 'width': '{}%'.format(len(
#                       example_prediction.columns)), 'textOverflow': 'ellipsis', 'overflow': 'hidden'},
#                   page_size=10,
#                   style_data={'border': '1px solid blue',
#                               'whiteSpace': 'normal',
#                               'height': 'auto',
#                               }
#                   )
#                  ]
# App instantiation
app = dash.Dash(__name__)
application = app.server
#  external_stylesheets=[
#     dbc.themes.CYBORG,
# ],
# Layout
app.layout = html.Div(children=[html.H1(id='Header', children=['Summary Statistics'], style={'textAlign': 'center'}),
                                dash_table.DataTable
                                (id='summary_statistics',
                                 data=summary_statistics.to_dict('records'),
                                 columns=[{"name": i, "id": i}
                                          for i in summary_statistics.columns],
                                 style_cell={'textAlign': 'center', 'width': '{}%'.format(len(
                                     summary_statistics.columns))},
                                 page_size=33,
                                 style_header={
                                     'backgroundColor': 'rgb(30, 30, 30)',
                                     'color': 'white'
                                 },
                                 fixed_columns={'headers': True, 'data': 1},
                                 sort_action='native',
                                 filter_action='native',
                                 
                                 style_data={'border': '1px solid grey',
                                             'whiteSpace': 'normal',
                                             'height': 'auto',
                                             'lineHeight': '15px',
                                             'backgroundColor': 'rgb(50, 50, 50)',
                                             'color': 'white'
                                             },
                                 style_table={'minWidth': '100%'},
                                 ),
                                html.H1(id='Second Header', children=['Predictions'], style={'textAlign': 'center'}),
                                dash_table.DataTable
                                (id='Predictions',
                                 data=example_prediction.to_dict('records'),
                                 columns=[{"name": i, "id": i}
                                          for i in example_prediction.columns],
                                 style_cell={'textAlign': 'center', 'width': '{}%'.format(len(
                                     example_prediction.columns))},
                                 page_size=33,
                                 style_header={
                                     'backgroundColor': 'rgb(30, 30, 30)',
                                     'color': 'white'
                                 },
                                 fixed_columns={'headers': True, 'data': 1},
                                 sort_action='native',
                                 filter_action='native',
                                 
                                 style_data={'border': '1px solid grey',
                                             'whiteSpace': 'normal',
                                             'height': 'auto',
                                             'lineHeight': '15px',
                                             'backgroundColor': 'rgb(50, 50, 50)',
                                             'color': 'white'
                                             },
                                 style_table={'minWidth': '100%'},
                                 )
                                
                                ])
# You will need to put this line at the bottom of your code to run #the application.
if __name__ == '__main__':
    application.run(debug=True)
