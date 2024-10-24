from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """
    <form action="/crawl" method="post">
        <label>검색할 키워드: </label>
        <input type="text" name="keyword">
        <input type="submit" value="크롤링 시작">
    </form>
    """


if __name__ == "__main__":
    app.run()
