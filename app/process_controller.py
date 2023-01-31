from sqlalchemy_get_or_create import get_or_create
from .models.transaction import Transaction
from .models.recipient import Recipient
from .models.type import Type
from sqlalchemy import func


class ProcessController():    
    def __init__(self, db, line):
        self.db    = db
        self.line  = line
        self.type  = line[0]
        self.date  = line[1:9]
        self.cpf   = line[19:30]
        self.card  = line[30:42]
        self.hour  = line[42:48]
        self.owner = line[48:62]
        self.name  = line[62:81]
        self.value = int(line[9:19]) / 100
    
        
    def return_type(self):
        type_obj = Type.query.filter_by(number=int(self.type)).first()
        
        return type_obj
    
    
    def recipient_handle(self):
        recipient = get_or_create(
            self.db.session,
            Recipient, 
            owner=self.owner,
            cpf=self.cpf,
            name=self.name
        )
                    
        recipient_obj = Recipient.query.filter_by(cpf=self.cpf, name=self.name).first()
        
        return recipient_obj
    
    
    def process_transaction(self):
        type_obj = self.return_type()
        recipient_obj = self.recipient_handle()      
        
        transaction = Transaction(
            type_id=type_obj.id,
            date=self.date,
            value=self.value,
            card=self.value,
            hour=self.hour,
            recipient_id=recipient_obj.id,
        )
        
        self.db.session.add(transaction)
        self.db.session.commit()
        
        transaction_obj = Transaction.query.filter_by(
            hour=transaction.hour,
            date=transaction.date
        ).first()
        
        return transaction_obj
    
    @classmethod
    def transactions_by_recipient(cls, db):
        recipients = Recipient.query.all()
        
        filtered_transactions = dict()
        
        for recipient in recipients:
            transactions = []
            balance = recipient.balance()
            for transaction in recipient.transactions:
                transactions.append(transaction)
            
            filtered_transactions[recipient.name] = {"transactions": transactions, **recipient.balance()}
            
                
        return filtered_transactions
