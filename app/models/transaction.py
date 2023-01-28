from ..database import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey("type.id"))
    date = db.Column(db.Date)
    value = db.Column(db.Float)
    recipient_id = db.Column(db.Integer, db.ForeignKey("recipient.id"))
    card = db.Column(db.String(12))
    hour = db.Column(db.Time)
    
    type = db.relationship("Type", back_populates="transactions")
    recipient = db.relationship("Recipient", back_populates="transactions")
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type.to_dict(),
            'date': self.date,
            'value': self.value,
            'recipient': self.recipient.to_dict(),
            'card': self.card,
            'hour': self.hour.strftime("%H:%M:%S")
        }
    