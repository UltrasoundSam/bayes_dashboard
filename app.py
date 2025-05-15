from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from bayes_dashboard import create_layout

def main():
    # Create app
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Bayes' Rule Dashboard"
    app.layout = create_layout(app)
    app.run(debug=True)


if __name__ == '__main__':
    main()
