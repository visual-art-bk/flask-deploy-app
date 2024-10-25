from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>hello wordl</h1>"

if __name__ == "__main__":
    app.run()
