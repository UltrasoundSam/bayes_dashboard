from dash import html, Dash
from dash import Output, Input
from . import ids

def render(app: Dash) -> html.Div:
    '''Renders information about Marginal to screen
    '''
    @app.callback(
        Output(ids.MARGINAL_RESULTS, 'children'),
        [Input(ids.PRIOR_SLIDER, "value"),
         Input(ids.LIKE_SLIDER, "value"),
         Input(ids.FALSE_SLIDER, "value")]
    )
    def update_marginal(prior: int,
                        likelihood: int,
                        false_positive: int) -> html.Div:
        '''Calculates probability of people that fit the
        evidence'''

        # Calculate True positives
        true_positives = (prior/100)*(likelihood/100)
        false_positives = ((100 - prior)/100) * (false_positive/100)

        marginal = true_positives + false_positives

        return html.Div([
            html.P(f'We are likely to see the evidence at a rate of {marginal:.1%} from any group in population'),
            html.P(f'This consists of {true_positives:.1%} of the population in the true positive group'),
            html.P(f'And {false_positives:.1%} of the population in the false positive group')
        ])


    return html.Div(id=ids.MARGINAL_RESULTS)
