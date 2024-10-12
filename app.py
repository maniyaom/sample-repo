from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "error": "false",
        "message": "Home Page"
    })

@app.route('/ip', methods=['GET'])
def get_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return jsonify({
        "error": "false",
        "message": ip
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)
