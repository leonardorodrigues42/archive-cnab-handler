from flask import request, render_template, redirect, url_for, jsonify
from .process_controller import ProcessController
from .utils import allowed_file
from .database import db
import asyncio


def init_app(app):
    @app.route('/upload')
    def upload():
        return render_template("upload.html")
    
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        
        if 'file_upload' not in request.files:
            return 'No file part'

        file = request.files['file_upload']

        if file.filename == '':
            return 'No selected file'

        if file and allowed_file(file.filename):
            file_content = file.read()
            lines = file_content.splitlines()
            
            db.session.autoflush = False
            
            transactions = []
            
            for line in lines:
                line  = line.decode()
                if line:
                    transaction_obj = ProcessController(db, line).process_transaction()
            
            return redirect("/sucess")

        return 'Invalid file type'
    
    
    @app.route("/sucess")
    def sucess():
        if not request.referrer or not request.referrer.endswith("/upload"):
            return "Pagina restrita!"
                
        return render_template("sucess.html")
    
    @app.route("/transactions")
    def transactions_list():
        transactions_by_recipient = ProcessController.transactions_by_recipient(db)

        return render_template("transactions.html", transactions=transactions_by_recipient)
    
    
    @app.get('/')
    def home():
        return redirect("/upload")
    