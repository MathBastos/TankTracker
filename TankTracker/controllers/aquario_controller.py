from flask import Blueprint, render_template, redirect, url_for, request
from models import db, Aquario, AquarioTamanho
from flask_login import login_required

aquario = Blueprint("aquario", __name__, template_folder="./views/", static_folder="./static/", root_path="./")

@aquario.route("/")
@login_required
def aquario_index():
    return render_template("aquario/listagem.html", title="Aquário")

@aquario.route("/cadastro")
@login_required
def aquario_cadastro():
    return render_template("/aquario/cadastro.html", title = "Aquário", url="/aquario/salvar", values=AquarioTamanho.listar_aquario_tamanhos())

@aquario.route("/salvar", methods=["POST"])
@login_required
def aquario_salvar():
    Aquario.salvar_aquario(request.form.get("nome"), request.form.get("id_tamanho"), request.form.get("quantidade_peixes"))
    return redirect(url_for('aquario.aquario_index'))

@aquario.route("/lista")
@login_required
def aquario_lista():
    return list(map(lambda x: x.json(), db.session.query(Aquario).all()))

@aquario.route("/editar/<int:id>")
@login_required
def aquario_editar(id):
    aquario = Aquario.listar_aquario(id)
    print(aquario)
    return render_template("/aquario/cadastro.html", title = "Aquário", url=f"/aquario/atualizar/{id}", values=AquarioTamanho.listar_aquario_tamanhos(), nome=aquario.nome, id_tamanho=aquario.id_tamanho, quantidade_peixes=aquario.quantidade_peixes)

@aquario.route("/atualizar/<int:id>", methods=["POST"])
@login_required
def aquario_atualizar(id):
    Aquario.atualizar_aquario(id, request.form.get("nome"), request.form.get("id_tamanho"), request.form.get("quantidade_peixes"))
    return redirect(url_for('aquario.aquario_index'))

@aquario.route("/deletar/<int:id>")
@login_required
def aquario_excluir(id):
    Aquario.deletar_aquario(id)
    return redirect(url_for('aquario.aquario_index'))