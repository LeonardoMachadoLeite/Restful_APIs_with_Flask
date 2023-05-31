from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/super_simple")
def super_simple():
    return jsonify(message="This is super simple.")

if __name__ == '__main__':
    app.run()