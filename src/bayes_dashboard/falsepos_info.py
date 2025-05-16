from dash import html


def render() -> html.Div:
    '''Renders information about false positive to screen
    '''
    fp_rate = 0.4
    msg = f'The False Positive Rate is {fp_rate:.1%}'
    return html.Div(msg)
