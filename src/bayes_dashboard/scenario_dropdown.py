from dash import dcc, html

from . import ids


def render() -> html.Div:
    '''Renders dropdown list
    '''
    dropdown = dcc.Dropdown(
        id=ids.SCENARIO_DROPDOWN,
        options=[
            {"label": "Farmer Steve", "value": "Steve"},
            {"label": "Test Efficacy", "value": "drugs"}],
        multi=False,
        value="Farmer Steve",
    )

    return html.Div(dropdown,
                    style={'textAlign': 'center'})
