from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    response_data = {
        'message': 'Hello, Flask!',
        'status': 'success',
        'data': {
            'website': 'gptonline.ai',
            'year': 2024
        }
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run()