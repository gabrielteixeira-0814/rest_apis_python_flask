from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# @app.route("/")
# def pessoas():
#     return jsonify({'nome' : 'Gabriel'})]

@app.route("/soma", methods=['POST'])
def soma():
    dados = json.loads(request.data)
    return jsonify(dados['valores'])

if __name__ == "__main__":
    app.run(debug=True)