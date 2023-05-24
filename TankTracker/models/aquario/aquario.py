from models.db import db
from models.aquario.aquario_tamanho import AquarioTamanho

class Aquario(db.Model):
    __tablename__ = "aquario"
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100))
    id_tamanho = db.Column(db.Integer, db.ForeignKey(AquarioTamanho.id))
    quantidade_peixes = db.Column(db.Integer())

    def listar_aquario(id):
        return Aquario.query.filter_by(id=id).first()

    def listar_aquarios():
        return Aquario.query.join(AquarioTamanho, AquarioTamanho.id == Aquario.id).add_columns(Aquario.id, Aquario.nome, AquarioTamanho.nome, Aquario.quantidade_peixes).all()

    def salvar_aquario(nome, id_tamanho, quantidade_peixes):
        db.session.add(Aquario(nome=nome, id_tamanho=id_tamanho, quantidade_peixes=quantidade_peixes))
        db.session.commit()

    def deletar_aquario(id):
        Aquario.query.filter_by(id=id).delete()
        db.session.commit()

    def atualizar_aquario(id, nome=None, id_tamanho=None, quantidade_peixes=None):
        Aquario.query.filter_by(id=id).update(dict(nome=nome, id_tamanho=id_tamanho, quantidade_peixes=quantidade_peixes))
        db.session.commit()
        
    def json(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Tamanho": AquarioTamanho.listar_aquario_tamanho(self.id_tamanho).nome,
            "Quantidade de Peixes": self.quantidade_peixes
        }