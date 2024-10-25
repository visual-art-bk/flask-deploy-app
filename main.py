from init import creat_app

app = creat_app()

@app.route("/", methods=["GET"])
def home():
    return "<h1>Hi Bk</h1>"

if __name__ == "__main__":
    app.run(debug=True)
