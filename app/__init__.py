from flask import Flask

# 앱 생성 및 설정
def create_app():
    app = Flask(__name__)

    # 라우터 등록
    from app.routes import main
    app.register_blueprint(main)

    return app