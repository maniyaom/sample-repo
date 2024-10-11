from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/ip', methods=['GET'])
def ip():
    return jsonify({
            "error": "false",
            "message": request.remote_addr
        })

if __name__ == '__main__':
    app.run(debug=True)