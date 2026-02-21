import boto3
from dash import Dash
from flask import redirect, request
from flask_login import current_user

from callbacks import switchboard
from index import lyt
from utils.auth import db, login_manager
from utils.routes import register_routes


def get_parameter(name):
    client = boto3.client("ssm", region_name="us-east-1")
    return client.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]


app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = lyt

switchboard(app)

server = app.server
server.secret_key = get_parameter("/ab-v2/flask-url")
server.config["SQLALCHEMY_DATABASE_URI"] = get_parameter("/ab-v2/db-url")
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(server)
login_manager.init_app(server)
login_manager.login_view = "/login"

with server.app_context():
    db.create_all()

register_routes(server)


@server.before_request
def require_login():
    allowed = ["/login", "/signup"]
    if not current_user.is_authenticated:
        if request.path in allowed or request.path.startswith("/_dash"):
            return None
        return redirect("/login")


if __name__ == "__main__":
    # app.run(debug=True, port="8050")  # for local development
    app.run(port=8050)  # for EC2 instance
