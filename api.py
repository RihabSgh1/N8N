from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the simple API!"

@app.route('/postdata', methods=['POST'])
def post_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    return jsonify({'you_sent': data}), 200

if __name__ == '__main__':
    app.run(debug=True)
