from flask import Flask, redirect
from models.db import db, instance
from models import Usuario, AquarioTamanho
from models.login import login_manager
from controllers import aquario, login, usuario

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/')

def create_app():
    return Flask(__name__, template_folder="./views/", static_folder="./static/", root_path="./")

def register_blueprints(app):
    app.register_blueprint(login, url_prefix='/')
    app.register_blueprint(aquario, url_prefix='/aquario')
    app.register_blueprint(usuario, url_prefix='/usuario')

def prepare_app():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    app.config['SECRET_KEY'] = 'secrete-key'
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        Usuario.salvar_usuario("admin", "admin@admin.com", "admin", "admin")
        AquarioTamanho.salvar_aquario_tamanho("pequeno")
        AquarioTamanho.salvar_aquario_tamanho("médio")
        AquarioTamanho.salvar_aquario_tamanho("grande")
    register_blueprints(app)
    login_manager.init_app(app)
    return app