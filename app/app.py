from flask import Flask, jsonify
import socket, os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "app": "DevOps CI/CD Project",
        "author": "Balaji K.",
        "hostname": socket.gethostname(),
        "version": os.environ.get("APP_VERSION", "1.0.0")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
