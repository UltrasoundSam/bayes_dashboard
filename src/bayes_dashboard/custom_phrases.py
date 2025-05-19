PHRASES = {
    'Steve': {
        'prior': 'of the population are librarians',
        'likelihood': 'of librarians are shy',
        'false_pos': 'of farmers are shy',
        'marginal': 'What percentage of the total population are shy?',
        'posterior': 'What percentage of shy people are librarians?'
    },
    'drugs': {
        'prior': ' of the population have the disease',
        'likelihood': 'The sensitivity of the test is',
        'false_pos': 'The false positive rate of the test is',
        'marginal': 'What percentage of the total population tested positive?',
        'posterior': 'What is the change of having the disease given a positive test?'  # noqa: E501
    },
    'bayes': {
        'prior': 'is your prior expectation',
        'likelihood': 'The likelihood is',
        'false_pos': 'The false positive Rate is',
        'marginal': 'We are likely to see evidence from the total population at a rate of...',  # noqa: E501
        'posterior': 'What is probability of hypothesis being true given the evidence?'  # noqa: E501
    }
}
