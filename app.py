from flask import Flask, request, jsonify, render_template
import ollama
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # Allow frontend to call API

# Serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API route for chat
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = ollama.generate(model="mistral", prompt=prompt)

    return jsonify({"response": response["response"]})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
