import plotly.graph_objects as go
from dash import dcc, html, Dash
from dash import Output, Input

from . import ids

def render(app: Dash) -> html.Div:
    '''Renders nice graph
    '''
    @app.callback(
        Output(ids.BAYES_GRAPH, "figure"),
        [Input(ids.PRIOR_SLIDER, "value")]
    )
    def display_graph(prior: int) -> go.Figure:
        '''Creates and formats geometric view of Bayes
        theorem
        '''
        fig = go.Figure()
        fig.update_layout(xaxis_range=[0, 100])
        fig.update_layout(yaxis_range=[0, 100])
        fig.add_vrect(x0=0, x1=prior, exclude_empty_subplots=False,
                      line_width=0, fillcolor="red", opacity=0.5)
        fig.add_vrect(x0=prior, x1=100, exclude_empty_subplots=False,
                      line_width=0, fillcolor="blue", opacity=0.5)

        return fig

    comp = html.Div(dcc.Graph(id=ids.BAYES_GRAPH))
    return comp