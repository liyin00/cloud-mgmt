from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route("/useless", methods=['GET'])
def hello():
    return "good day sir! useless is up!!!"

if __name__ == '__main__':
    print("useless")
    app.run(host='0.0.0.0', port=5050, debug=True)