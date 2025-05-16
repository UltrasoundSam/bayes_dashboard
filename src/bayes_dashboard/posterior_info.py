from dash import html, Dash
from dash import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    '''Renders information about posterior to screen
    '''
    @app.callback(
        Output(ids.POSTERIOR_INFO, 'children'),
        [Input(ids.PRIOR_SLIDER, "value"),
         Input(ids.LIKE_SLIDER, "value"),
         Input(ids.FALSE_SLIDER, "value")]
    )
    def bayes_rule(prior: int,
                   likelihood: int,
                   false_positive: int) -> html.Div:
        '''Applies Bayes rule to update out prediction'''
        # Calculate True positives
        true_positives = (prior/100)*(likelihood/100)
        false_positives = ((100 - prior)/100) * (false_positive/100)

        # Calculates Marginal
        marginal = true_positives + false_positives

        posterior = true_positives / (marginal)

        return html.Div([
            html.P(f'We should update our beliefs from {prior:.1f}% to {posterior:.1%}')
        ])


    return html.Div(id=ids.POSTERIOR_INFO)
