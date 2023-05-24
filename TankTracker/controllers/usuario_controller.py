from flask import Blueprint, render_template, redirect, url_for, request
from models import db, Usuario
from flask_login import login_required

usuario = Blueprint("usuario", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

@usuario.route("/")
@login_required
def usuario_index():
    return render_template("usuario/listagem.html", title="Aquário")

@usuario.route("/cadastro")
@login_required
def usuario_cadastro():
    return render_template("/usuario/cadastro.html", title = "Usuário", url="/usuario/salvar")

@usuario.route("/salvar", methods=["POST"])
@login_required
def usuario_salvar():
    Usuario.salvar_usuario(request.form.get("nome"), request.form.get("email"), request.form.get("usuario"), request.form.get("senha"))
    return redirect(url_for('usuario.usuario_index'))

@usuario.route("/lista")
@login_required
def usuario_lista():
    return list(map(lambda x: x.json(), db.session.query(Usuario).all()))

@usuario.route("/editar/<int:id>")
@login_required
def usuario_editar(id):
    usuario = Usuario.listar_usuario(id)
    return render_template("/usuario/cadastro.html", title = "Usuário", url=f"/usuario/atualizar/{id}", nome=usuario.nome, email=usuario.email, usuario=usuario.usuario, senha=usuario.senha)

@usuario.route("/atualizar/<int:id>", methods=["POST"])
@login_required
def usuario_atualizar(id):
    Usuario.atualizar_usuario(id, request.form.get("nome"), request.form.get("email"), request.form.get("usuario"), request.form.get("senha"))
    return redirect(url_for('usuario.usuario_index'))

@usuario.route("/deletar/<int:id>")
@login_required
def usuario_excluir(id):
    Usuario.deletar_usuario(id)
    return redirect(url_for('usuario.usuario_index'))