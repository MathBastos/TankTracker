from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from models import Usuario

login = Blueprint("login", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

@login.route("/")
def login_index():
    if current_user.is_authenticated:
        return redirect(url_for("aquario.aquario_index"))
    else:
        return render_template("login.html")

@login.route("/autenticar", methods=["POST"])
def login_autenticar():
    usuario = Usuario.query.filter_by(usuario=request.form.get("usuario"), senha=request.form.get("senha")).first()
    print(request.form)
    print(request.form.get("usuario"))
    print(request.form.get("senha"))
    print(usuario)
    if usuario:
        login_user(usuario)
        return redirect(url_for("aquario.aquario_index"))
    else:
        return render_template("login.html", error=True)

@login.route("/logout")
@login_required
def login_logout():
    logout_user()
    return redirect(url_for("login.login_index"))
