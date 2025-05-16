from dash import html, dcc, Dash
from dash import Output, Input

from . import ids


def render(app: Dash) -> html.Div:
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
        [Input(ids.PRIOR_SLIDER, component_property="value")]
    )
    def update_priors(slider_value: int) -> str:
        '''Updates priors text'''
        msg = f'The prior is {slider_value:.1f}%'
        return msg


    return html.Div([msg, slider],
                    style={'textAlign': 'center',
                           'width': '32%',
                           'margin-left': '34%'})
