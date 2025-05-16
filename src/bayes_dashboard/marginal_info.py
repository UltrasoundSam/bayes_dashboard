from dash import html


def render() -> html.Div:
    '''Renders information about Marginal to screen
    '''
    marginal = 0.4
    msg = f'The Marginal is {marginal:.1%}'
    return html.Div(msg)
