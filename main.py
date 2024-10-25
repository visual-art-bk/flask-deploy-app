from app import create_app

app = create_app()

@app.route("/", methods=["GET"])
def home():
    return "<h1>Hi Bk 777</h1>"

if __name__ == "__main__":
    app.run(debug=True)
