from flask import Flask, request, jsonify
from main import get_result

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Leia o README para entender como encontrar o jogo para você!</p>"

@app.route("/query")
def query():
    # Extract the 'query' parameter from the URL
    query_text = request.args.get('query', '')
    query_text = query_text.replace('-', ' ')  # Replace dashes with spaces

    # Process the query using the imported function
    result_json = get_result(query_text)

    # Return the JSON result to the browser
    return jsonify(result_json)

if __name__ == "__main__":
    app.run(port="7591", debug=True)
