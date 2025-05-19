import dash_bootstrap_components as dbc
from dash import html, dcc, Dash
from dash import Output, Input

from . import ids
from .custom_phrases import PHRASES


def render(app: Dash, graph_size: int) -> html.Div:
    '''Renders information about likelihood to screen
    '''
    # Create Slider
    slider = dcc.Slider(
        id=ids.LIKE_SLIDER,
        min=0,
        max=100,
        step=1,
        value=40,
        marks={i: f'{i}%' for i in range(0, 101, 10)},
        vertical=True,
        verticalHeight=graph_size
    )

    # Create label
    msg = html.Label(' ', id=ids.LIKE_INFO,
                     style={"writingMode": "vertical-lr",
                            "textOrientation": "mixed",
                            "transform": "rotate(180deg)"})

    # Create callball
    @app.callback(
        Output(ids.LIKE_INFO, "children"),
        [Input(ids.LIKE_SLIDER, "value"),
         Input(ids.SCENARIO_DROPDOWN, 'value')]
    )
    def update_likelihoods(slider_value: int,
                           scenario: str) -> str:
        '''Updates likelihood test info'''
        cust_phrase = PHRASES[scenario]['likelihood']

        if scenario == 'Steve':
            msg = f'{slider_value:.0f}% {cust_phrase}'
        else:
            msg = f'{cust_phrase} {slider_value:.0f}%'
        return msg

    # Arrange format
    fmt = dbc.Row(
        [
            dbc.Col(html.Div(msg)),
            dbc.Col(html.Div(slider))
        ],
        align='center',
        justify='end',
        className="g-0"
    )

    return html.Div(fmt,
                    style={'margin-left': '70%'})
