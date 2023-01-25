from ..database import db
from sqlalchemy import Numeric


class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpf = db.Column(Numeric(10, 0))
    owner = db.Column(db.String(255))

    transactions = db.relationship("Transaction", back_populates="recipient", lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'owner': self.owner,
            'transaction': [transaction.to_dict() for trasaction in self.transactions]
        }
