from flask import Flask

app = Flask(__name__)

# 라우팅 모듈 등록
from app.routes import main

app.register_blueprint(main)

if __name__ == "__main__":
    app.run()
