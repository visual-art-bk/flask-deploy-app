# app/routes.py
from flask import Blueprint, request, jsonify

# 블루프린트 생성
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask App!"

