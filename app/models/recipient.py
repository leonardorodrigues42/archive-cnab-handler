from ..database import db
from sqlalchemy import Numeric


class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpf = db.Column(db.String(11))
    owner = db.Column(db.String(255))

    transactions = db.relationship("Transaction", back_populates="recipient")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'owner': self.owner,
        }
        
    def balance(self):
        total = 0
        
        for transaction in self.transactions:
            if transaction.type.nature == "Entrada":
                total += transaction.value
                
            else:
                total -= transaction.value
        
        return {
            'balance': total
        }
        
    # def transactions
