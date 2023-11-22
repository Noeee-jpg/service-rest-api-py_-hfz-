from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello, World!'

@app.route("/login", methods=["GET"])
def login():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)
