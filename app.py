from flask import Flask, jsonify
from app import create_app

# app = Flask(__name__)
app = create_app()


if __name__ == "__main__":
    app.run()
