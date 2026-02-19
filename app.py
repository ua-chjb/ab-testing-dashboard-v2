from dash import Dash

from callbacks import switchboard
from index import lyt

app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = lyt

switchboard(app)

server = app.server

if __name__ == "__main__":
    app.run(debug=True, port="8050")  # for local development
    # app.run() # for EC2 instance
