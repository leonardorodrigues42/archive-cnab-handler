from flask import Flask, jsonify, request, render_template
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
                    transactions.append(transaction_obj.to_dict())
            return jsonify(transactions), 201

        return 'Invalid file type'
    

    @app.route("/transactions")
    def transactions_list():
        transactions = ProcessController.transactions_by_recipient(db)    

        return jsonify(transactions), 201
    
    
    @app.get('/')
    def home():
        tipos = {"message": "funfou aqui"}

        return tipos, 200
    