from flask import Flask, jsonify, request
from .models.transaction import Transaction
from .models.type import Type
from .models.recipient import Recipient

def init_app(app):
    @app.get('/')
    def home():
        tipos = {"message": "funfou aqui"}

        return tipos, 200
