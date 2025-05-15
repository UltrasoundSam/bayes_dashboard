from dash import Dash, html

from . import scenario_dropdown

def create_layout(app: Dash) -> html.Div:
    '''Defines layout for Dashboard
    '''
    layout = html.Div(
        className="app-div",
        children=[
            html.H1("Interactive Bayes Theorem Explorer",
                    style={'text-align': 'center'}),
            html.Hr(),
            html.Div(
                className='dropdown-container',
                children=[
                    scenario_dropdown.render()
                ])
        ]
    )

    return layout
