from flask import Blueprint, request, send_file

# 블루프린트 생성
main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
    return """
    <form action="/crawl" method="post">
        <label>검색할 키워드: </label>
        <input type="text" name="keyword">
        <input type="submit" value="크롤링 시작">
    </form>
    """
