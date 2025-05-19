from dash import html, dcc, Dash
from dash import Output, Input

from . import ids
from .custom_phrases import PHRASES


def render(app: Dash, graph_size: int) -> html.Div:
    '''Renders information about prior to screen
    '''
    # Create Slider
    slider = dcc.Slider(
        id=ids.PRIOR_SLIDER,
        min=0,
        max=100,
        step=1,
        value=30,
        marks={i: f'{i}%' for i in range(0, 101, 10)}
    )

    msg = html.Label('The prior is 30 %', id=ids.PRIOR_INFO)

    @app.callback(
        Output(ids.PRIOR_INFO, "children"),
        [Input(ids.PRIOR_SLIDER, component_property="value"),
         Input(ids.SCENARIO_DROPDOWN, 'value')]
    )
    def update_priors(slider_value: int,
                      scenario: str) -> str:
        '''Updates priors text'''
        cust_phase = PHRASES[scenario]['prior']
        msg = f'{slider_value:.0f}% {cust_phase}'
        return msg

    return html.Div([msg, slider],
                    style={'textAlign': 'center',
                           'width': graph_size,
                           'margin-left': '34%'})
