from flask import Flask
from flask_migrate import Migrate
from .database import db
from .models.type import Type
from . import routes
from . import database

def popular_database(app):   
    with app.app_context():    
        stored_data = db.session.query(Type).options(db.joinedload(Type.transactions)).all()
        if len(stored_data):
            None
        else:
            data = [
                (1,	"Débito", "Entrada"),
                (2,	"Boleto", "Saída"),
                (3,	"Financiamento", "Saída"),
                (4,	"Crédito", "Entrada"),
                (5,	"Recebimento Empréstimo", "Entrada"),
                (6,	"Vendas", "Entrada"),
                (7,	"Recebimento TED", "Entrada"),
                (8,	"Recebimento DOC", "Entrada"),
                (9,	"Aluguel", "Saída"),
            ]
        
            for item in data:
                type = Type(number=item[0], description=item[1], nature=item[2])
                db.session.add(type)
                
            db.session.commit()

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_FOLDER'] = 'templates'
    app.config['JSON_AS_ASCII'] = False
    
    database.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    migrate = Migrate(app, db)
    
    routes.init_app(app)
       
    popular_database(app)
    
    return app
