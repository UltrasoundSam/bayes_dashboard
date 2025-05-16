import plotly.express as px
import pandas as pd
from dash import dcc, html

from . import ids

def render() -> html.Div:
    '''Renders nice graph
    '''
    data = {'col1': [1, 2, 3, 4], 'col2': [1, 4, 9, 16]}
    df = pd.DataFrame(data=data)
    fig = px.bar(data_frame=df)

    comp = html.Div(dcc.Graph(figure=fig), id=ids.BAYES_GRAPH)
    return comp