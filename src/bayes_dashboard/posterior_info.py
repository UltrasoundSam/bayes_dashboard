from dash import html, Dash
from dash import Input, Output

from . import ids
from .custom_phrases import PHRASES


def render(app: Dash) -> html.Div:
    '''Renders information about posterior to screen
    '''
    @app.callback(
        Output(ids.POSTERIOR_INFO, 'children'),
        [Input(ids.PRIOR_SLIDER, "value"),
         Input(ids.LIKE_SLIDER, "value"),
         Input(ids.FALSE_SLIDER, "value"),
         Input(ids.SCENARIO_DROPDOWN, 'value')]
    )
    def bayes_rule(prior: int,
                   likelihood: int,
                   false_positive: int,
                   scenario: str) -> html.Div:
        '''Applies Bayes rule to update out prediction'''
        # Calculate True positives
        true_positives = (prior/100)*(likelihood/100)
        false_positives = ((100 - prior)/100) * (false_positive/100)

        # Calculates Marginal
        marginal = true_positives + false_positives

        # Applying Bayes Rule
        posterior = true_positives / (marginal)

        # Getting custom message from dict
        cust_msg = PHRASES[scenario]['posterior']

        return html.Div([
            html.H4('Posterior, P(H|E)'),
            html.P(cust_msg),
            html.H3(f'{posterior:.1%}'),
            html.P("Calculated using Bayes' Theorem as:"),
            html.H5(f'{true_positives:.1%}',
                    style={'background-color': '#f2767b',
                           'width': '15%',
                           'margin-left': '42.5%'}),
            html.Hr(style={'width': '32%',
                           'margin-left': '34%'}),
            html.H5(
                [
                    html.Span(f'{true_positives:.1%}',
                              style={'background-color': '#f2767b'}),
                    html.Span(' + '),
                    html.Span(f'{false_positives: .1%}',
                              style={'background-color': '#7276fb'})
                ]
            )
        ], style={'textAlign': 'center'})

    return html.Div(id=ids.POSTERIOR_INFO)
