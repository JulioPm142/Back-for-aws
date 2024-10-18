from flask import Flask, jsonify
from flask_cors import CORS  # Importa o CORS

app = Flask(__name__)
CORS(app)  # Ativa o CORS para todas as rotas

@app.route('/api/data', methods=['GET'])
def get_data():
    response = {
        'message': 'Teste',
        'data': {
            'value1': 123,
            'value2': 456
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
