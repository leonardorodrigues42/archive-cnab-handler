from ..database import db
from sqlalchemy.dialects.postgresql import ENUM

class Type(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.Integer())
    description = db.Column(db.String(32))
    nature = db.Column(ENUM("Entrada", "Saída", name="nature_enum"))
    
    transactions = db.relationship("Transaction", back_populates="type", lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'number': self.number,
            'transactions_count': len(self.transactions)
        }
