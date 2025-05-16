from dash import html


def render() -> html.Div:
    '''Renders information about likelihood to screen
    '''
    likelihood = 0.4
    msg = f'The likelihood is {likelihood:.1%}'
    return html.Div(msg)
