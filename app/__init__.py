from flask import Flask

# Flask 앱을 생성하고 설정하는 함수
def create_app():
    app = Flask(__name__)

    # 라우팅 모듈 등록
    from .routes import main

    app.register_blueprint(main)

    return app
