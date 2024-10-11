from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "error": "false",
        "message": "Home Page"
    })

@app.route('/ip', methods=['GET'])
def get_ip():
    return jsonify({
        "error": "false",
        "message": request.remote_addr
    })

if __name__ == '__main__':
    app.run(debug=True)
