from flask import redirect, url_for, request, flash, render_template
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

from utils.auth import db, User


def register_routes(server):

    @server.route("/login", methods=["GET", "POST"])
    def login():
        from utils.forms import LoginForm

        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect("/")
            flash("Invalid username or password")
        return render_template("login.html", form=form)

    @server.route("/signup", methods=["GET", "POST"])
    def signup():
        from utils.forms import SignupForm

        form = SignupForm()
        if form.validate_on_submit():
            existing = User.query.filter_by(username=form.username.data).first()

            if existing:
                flash("Username already taken")
                return render_template("signup.html", form=form)
            user = User(
                id=str(uuid.uuid4()),
                username=form.username.data,
                password_hash=generate_password_hash(form.password.data),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect("/")
        return render_template("signup.html", form=form)

    @server.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect("/login")
