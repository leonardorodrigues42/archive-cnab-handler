import os
from flask_sqlalchemy import SQLAlchemy
import dotenv

dotenv.load_dotenv()

db = SQLAlchemy()

PASSWORD = os.getenv("POSTGRES_PASSWORD")
USER = os.getenv("POSTGRES_USER")
DB = os.getenv("POSTGRES_DB")

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USER}:{PASSWORD}@db:5432/{DB}"
    db.init_app(app)
    
    return app
