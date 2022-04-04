import dash
from dash import dcc
from dash import html
from dash import Dash, dash_table, html, dcc
#import boto3
import pandas as pd


# reading data
df_historical_matchups = pd.read_csv('data/historical_matchups.csv')
#prediction_df_list = [pd.read_csv(f'frontend/assets/{x}.csv') for x in range(6)]
#summary_statistics = pd.read_csv()
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

# App instantiation
app = dash.Dash(__name__)
application = app.server

# Layout
app.layout = html.Div(children=[html.H1(id='Header', children=['Black Mamba'], style={'textAlign': 'center'}),

                                dash_table.DataTable(id='example_prediction', data=example_prediction.to_dict('records'), columns=[{"name": i, "id": i} for i in example_prediction.columns], style_cell={'textAlign': 'left', 'width': '{}%'.format(len(example_prediction.columns)),
        'textOverflow': 'ellipsis',
        'overflow': 'hidden'}, page_size=10, style_data={
                                    'whiteSpace': 'normal',
                                    'height': 'auto',
                                },  css=[{'selector': 'table', 'rule': 'table-layout: fixed'}], 
                                    # style_cell_conditional=[
                                    # {'if': {'column_id': 'Statistics'},
                                    #  'width': '10%'}, {'if': {'column_id': 'Winner'},
                                    #                    'width': '10%'}, {'if': {'column_id': 'Loser'},
                                    #                                      'width': '10%'}]
                                    )
                                ])
# You will need to put this line at the bottom of your code to run #the application.
if __name__ == '__main__':
    application.run(debug=True)
