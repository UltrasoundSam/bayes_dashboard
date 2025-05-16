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
        value=30,
        marks={i: f'{i}%' for i in range(0, 101, 10)},
        vertical=True
    )

    # Create label
    msg = html.Label('The prior is 80 %', id=ids.LIKE_INFO)

    # Create callball
    @app.callback(
        Output(ids.LIKE_INFO, "children"),
        [Input(ids.LIKE_SLIDER, "value")]
    )
    def update_likelihoods(slider_value: int) -> str:
        '''Updates likelihood test info'''
        msg = f'The likelihood is {slider_value:.1f}%'
        return msg


    return html.Div([msg, slider],
                     style={'textAlign': 'center',
                            'width': '66%',
                            'margin-left': '16%'})
