import dash_bootstrap_components as dbc
from dash import html, dcc, Dash
from dash import Output, Input

from . import ids
from .custom_phrases import PHRASES


def render(app: Dash) -> html.Div:
    '''Renders information about false positive to screen
    '''
    # Create Slider
    slider = dcc.Slider(
        id=ids.FALSE_SLIDER,
        min=0,
        max=100,
        step=1,
        value=10,
        vertical=True,
        verticalHeight=600,
        marks={i: f'{i}%' for i in range(0, 101, 10)}
    )

    # Create label
    msg = html.Label('The prior is 80 %', id=ids.FALSE_INFO,
                     style={"transform": "rotate(90deg)"})

    # Create callback
    @app.callback(
        Output(ids.FALSE_INFO, "children"),
        [Input(ids.FALSE_SLIDER, "value"),
         Input(ids.SCENARIO_DROPDOWN, 'value')]
    )
    def update_falsepos(slider_value: int,
                        scenario: str) -> str:
        '''Updates false positive info'''
        cust_phase = PHRASES[scenario]['false_pos']
        msg = f'{slider_value:.0f}% {cust_phase}'
        return msg

    # Arrange format
    fmt = dbc.Row(
        [
            dbc.Col(html.Div(slider), width=2),
            dbc.Col(html.Div(msg), width=10),

        ],
        align='center',
        justify='start'
    )

    return html.Div(fmt)
