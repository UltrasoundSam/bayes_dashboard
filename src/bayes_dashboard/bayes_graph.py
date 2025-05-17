import plotly.graph_objects as go
from dash import dcc, html, Dash
from dash import Output, Input

from . import ids


def render(app: Dash) -> html.Div:
    '''Renders nice graph
    '''
    @app.callback(
        Output(ids.BAYES_GRAPH, "figure"),
        [Input(ids.PRIOR_SLIDER, "value"),
         Input(ids.LIKE_SLIDER, "value"),
         Input(ids.FALSE_SLIDER, "value")]
    )
    def display_graph(prior: int,
                      likelihood: int,
                      false_positive: int) -> go.Figure:
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

        # Subselect True Positives
        fig.add_shape(type='rect',
                      x0=0, y0=likelihood, x1=prior, y1=100,
                      line=dict(color='black', width=0.75),
                      fillcolor='black',
                      opacity=0.3)

        # Subselect False Positives
        fig.add_shape(type='rect',
                      x0=prior, y0=false_positive, x1=100, y1=100,
                      line=dict(color='black', width=0.75),
                      fillcolor='black',
                      opacity=0.3)

        fig.update_layout(width=615, height=600,
                          margin=dict(l=0, r=0, t=0, b=0))

        return fig

    comp = html.Div(dcc.Graph(id=ids.BAYES_GRAPH))
    return comp
