from flask import Flask, request, jsonify
from main import get_result

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Leia o README para entender como encontrar o jogo para você!</p>
            <a href="https://github.com/RaulRangelMB/NLP-APS01-SteamRecommendation" target="_blank">Repositorio</a>"""

@app.route("/query")
def query():
    query_text = request.args.get('query', '')
    query_text = query_text.replace('-', ' ')

    result_json = get_result(query_text)

    return jsonify(result_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7591, debug=True)