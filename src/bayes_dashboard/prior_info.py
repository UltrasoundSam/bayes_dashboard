from dash import html


def render() -> html.Div:
    '''Renders information about prior to screen
    '''
    prior = 0.4
    msg = f'The prior is {prior:.1%}'
    return html.Div(msg)
