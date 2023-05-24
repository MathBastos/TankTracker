from models.db import db

class AquarioTamanho(db.Model):
    __tablename__ = "aquario_tamanho"
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100))

    def listar_aquario_tamanhos():
        return AquarioTamanho.query.all()

    def listar_aquario_tamanho(id):
        return AquarioTamanho.query.filter_by(id=id).first()

    def salvar_aquario_tamanho(nome):
        db.session.add(AquarioTamanho(nome=nome))
        db.session.commit()

    def deletar_aquario_tamanho(id):
        AquarioTamanho.query.filter_by(id=id).delete()
        db.session.commit()

    def atualizar_aquario_tamanho(id, nome):
        AquarioTamanho.query.filter_by(id=id).update(dict(nome=nome))
        db.session.commit()