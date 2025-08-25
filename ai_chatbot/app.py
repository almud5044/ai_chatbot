from flask import Flask, render_template, request, jsonify
from chatbot import get_ai_response  # importer AI-funksjonen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    bot_response = get_ai_response(user_message)  # AI-generert svar
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
