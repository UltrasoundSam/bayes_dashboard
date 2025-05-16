import dash_bootstrap_components as dbc
from dash import Dash, html

from . import scenario_dropdown, prior_info, likelihood_info
from . import falsepos_info, marginal_info, posterior_info
from . import bayes_graph

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
                        prior_info.render(app)
                    ]))),
                dbc.Row(
                    [
                        dbc.Col(html.Div(className='Likelihood',
                                         children=[likelihood_info.render(app)])),
                        dbc.Col(html.Div(className='BayesGraph',
                                         children=[bayes_graph.render(app)])),
                        dbc.Col(html.Div(className='FalsePositive',
                                         children=[falsepos_info.render(app)])),
                    ],
                    className="g-0"),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(html.Div(className='Marginal',
                                         children=[marginal_info.render(app)]),
                                         width=5),
                        dbc.Col(html.Div(className='Posterior',
                                         children=[posterior_info.render(app)]),
                                         width=5),
                    ],
                    className="g-0")
            ])
        ]
    )

    return layout
