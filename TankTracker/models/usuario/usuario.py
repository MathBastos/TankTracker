from models.db import db
from models.login import login_manager

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(30))
    email = db.Column(db.String(100))
    usuario = db.Column(db.String(30))
    senha = db.Column(db.String(30))

    def listar_usuarios():
        return Usuario.query.all()

    def listar_usuario(id):
        return Usuario.query.filter_by(id=id).first()

    def salvar_usuario(nome, email, usuario, senha):
        db.session.add(Usuario(nome=nome, email=email, usuario=usuario, senha=senha))
        db.session.commit()

    def deletar_usuario(id):
        Usuario.query.filter_by(id=id).delete()
        db.session.commit()

    def atualizar_usuario(id, nome, email, usuario, senha):
        Usuario.query.filter_by(id=id).update(dict(nome=nome, email=email, usuario=usuario, senha=senha))
        db.session.commit()

    def json(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Email": self.email,
            "Usuario": self.usuario
        }

    def is_authenticated(usuario):
        return True
    
    def is_active(usuario):
        return True
    
    def is_anonymous(usuario):
        return False
    
    @login_manager.user_loader
    def load_user(id):
        return Usuario.listar_usuario(id)

    def get_id(usuario):
        return str(usuario.id)
