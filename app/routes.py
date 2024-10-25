# app/routes.py
from flask import Blueprint, request, jsonify
from app.WebDriverManager import WebDriverManager
import time
# 블루프린트 생성
main = Blueprint('main', __name__)
wd = WebDriverManager()
driver = wd.get_driver()

@main.route('/')
def home():
    url = 'https://www.naver.com'
    print('Test driver 입니다.')
    driver.get(url)
    print(url, "열었습니다.")
    time.sleep(5)
    wd.close_driver()
    
    return "<h1>테스트완료</h1>"