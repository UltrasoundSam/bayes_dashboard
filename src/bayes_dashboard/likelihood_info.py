import dash_bootstrap_components as dbc
from dash import html, dcc, Dash
from dash import Output, Input

from . import ids


def render(app: Dash) -> html.Div:
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
        verticalHeight=600
    )

    # Create label
    msg = html.Label(' ', id=ids.LIKE_INFO,
                     style={"transform": "rotate(270deg)"})

    # Create callball
    @app.callback(
        Output(ids.LIKE_INFO, "children"),
        [Input(ids.LIKE_SLIDER, "value")]
    )
    def update_likelihoods(slider_value: int) -> str:
        '''Updates likelihood test info'''
        msg = f'The likelihood is {slider_value:.1f}%'
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
                    style={'margin-left': '80%'})
