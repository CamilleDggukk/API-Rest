from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint de teste
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# Endpoint para receber dados do front-end
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({'received_data': data})

# Endpoint para enviar dados para o front-end
@app.route('/api/data', methods=['GET'])
def send_data():
    data = {'key': 'value', 'number': 123}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
