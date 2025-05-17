from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from bayes_dashboard import create_layout


# Create app
app = Dash(external_stylesheets=[BOOTSTRAP])
app.title = "Bayes' Rule Dashboard"
app.layout = create_layout(app)
server = app.server


if __name__ == '__main__':
    app.run(debug=True)
