import os
from flask_sqlalchemy import SQLAlchemy
import dotenv

dotenv.load_dotenv()

db = SQLAlchemy()

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    
    return app
