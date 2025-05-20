from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Optional: for checking if server is alive
@app.route('/', methods=['GET'])
def index():
    return 'Server is running!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()

    if message == 'hi':
        response = 'Hello, Sean'
    else:
        response = "I didn't understand that."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)