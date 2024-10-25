from flask import Flask
# from app import create_app

# app = create_app()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>hello wordl</h1>"

if __name__ == "__main__":
    app.run()
