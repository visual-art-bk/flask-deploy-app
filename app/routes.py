from flask import Blueprint, request, jsonify

# 블루프린트 생성
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask App!"

# @main.route('/scrape', methods=['GET'])
# def scrape():
#     url = request.args.get('url')
#     if not url:
#         return jsonify({"error": "URL parameter is required"}), 400

#     data = get_web_data(url)  # Selenium 함수 호출
#     return jsonify(data)
