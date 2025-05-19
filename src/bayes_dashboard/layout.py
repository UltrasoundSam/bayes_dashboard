import dash_bootstrap_components as dbc
from dash import Dash, html

from . import scenario_dropdown, prior_info, likelihood_info
from . import falsepos_info, marginal_info, posterior_info
from . import bayes_graph

# Define some constants
MARGINAL_BACKGROUND = '#ADD8E6'
POSTERIOR_BACKGROUND = '#ebb07a'

RADIUS_LARGE = '25px'
GRAPH_SIZE = 600


def create_layout(app: Dash) -> html.Div:
    '''Defines layout for Dashboard
    '''
    layout = html.Div(
        className="app-div",
        children=[
            html.H1("Interactive Bayes Theorem Explorer",
                    style={'text-align': 'center'}),
            html.Hr(),
            html.Br(),
            html.Div([
                dbc.Row(dbc.Col(html.Div(
                    className='dropdown-container',
                    children=[
                        scenario_dropdown.render()
                    ]))),
                html.Br(),
                dbc.Row(dbc.Col(html.Div(
                    className='Prior',
                    children=[
                        prior_info.render(app, GRAPH_SIZE)
                    ]))),
                dbc.Row(
                    [
                        dbc.Col(html.Div(className='Likelihood',
                                         children=[likelihood_info.render(app, GRAPH_SIZE)])),  # noqa: E501
                        dbc.Col(html.Div(className='BayesGraph',
                                         children=[bayes_graph.render(app, GRAPH_SIZE)])),
                        dbc.Col(html.Div(className='FalsePositive',
                                         children=[falsepos_info.render(app, GRAPH_SIZE)])),  # noqa: E501
                    ]),
                html.Br(), html.Br(), html.Br(),
                dbc.Row(
                    [
                        dbc.Col(html.Div(className='Marginal',
                                         children=[marginal_info.render(app)]),
                                width={'size': 3},
                                style={'background-color': MARGINAL_BACKGROUND,
                                       'border-radius': RADIUS_LARGE}),
                        dbc.Col(html.Div(className='Posterior',
                                         children=[posterior_info.render(app)]),  # noqa: E501
                                width={'size': 3, 'offset': 1},
                                style={'background-color': POSTERIOR_BACKGROUND,
                                       'border-radius': RADIUS_LARGE}),
                    ], justify='center')
            ])
        ]
    )

    return layout
