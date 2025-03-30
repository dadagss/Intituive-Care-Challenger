# api/server.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df_operadoras = pd.read_csv('operadoras/operadoras.csv', sep=';', encoding='utf-8-sig')

@app.route('/api/operadoras', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('q', '')
    resultados = df_operadoras[
        df_operadoras['nome_fantasia'].str.contains(termo, case=False, na=False) |
        df_operadoras['razao_social'].str.contains(termo, case=False, na=False)
    ].head(50)
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)