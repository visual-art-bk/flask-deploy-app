# app/routes.py
from flask import Blueprint, request, jsonify
from app.selenium_utils import get_web_data  # Selenium 함수 임포트


# 블루프린트 생성
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask App!1"

@main.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    data = get_web_data(url)  # Selenium 함수 호출
    return jsonify(data)