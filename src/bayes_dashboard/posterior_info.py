from dash import html


def render() -> html.Div:
    '''Renders information about posterior to screen
    '''
    posterior = 0.4
    msg = f'The Posterior is {posterior:.1%}'
    return html.Div(msg)
