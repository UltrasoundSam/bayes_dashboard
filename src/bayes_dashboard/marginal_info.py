from dash import html, Dash
from dash import Output, Input

from . import ids
from .custom_phrases import PHRASES


def render(app: Dash) -> html.Div:
    '''Renders information about Marginal to screen
    '''
    @app.callback(
        Output(ids.MARGINAL_RESULTS, 'children'),
        [Input(ids.PRIOR_SLIDER, "value"),
         Input(ids.LIKE_SLIDER, "value"),
         Input(ids.FALSE_SLIDER, "value"),
         Input(ids.SCENARIO_DROPDOWN, 'value')]
    )
    def update_marginal(prior: int,
                        likelihood: int,
                        false_positive: int,
                        scenario: str) -> html.Div:
        '''Calculates probability of people that fit the
        evidence'''

        # Calculate True positives
        true_positives = (prior/100)*(likelihood/100)
        false_positives = ((100 - prior)/100) * (false_positive/100)

        marginal = true_positives + false_positives

        # Get custom message from dict
        cust_msg = PHRASES[scenario]['marginal']

        return html.Div([
            html.H4('Marginal/Evidence P(E)'),
            html.P(cust_msg),
            html.H3(f'{marginal:.1%}'),
            html.P('This percentage is comprised of the following groups:'),
            html.H5(
                [
                    html.Span(f'{true_positives:.1%}',
                              style={'background-color': '#f2767b',
                                     'margin': 0,
                                     'padding': 0,
                                     'border-radius': '5px'}),
                    html.Span(' + '),
                    html.Span(f'{false_positives: .1%}',
                              style={'background-color': '#7276fb',
                                     'border-radius': '5px'})
                ]
            )  # noqa: E501
        ], style={'textAlign': 'center'})

    return html.Div(id=ids.MARGINAL_RESULTS)
