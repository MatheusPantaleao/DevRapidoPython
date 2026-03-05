from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculo', methods=['POST'])
def calculo():
    dados = request.get_json()

    try:
        num1 = dados.get('num1')
        num2 = dados.get('num2')
        operador = dados.get('operador').strip()

        if operador not in ('+', '-', '*', '/'):
            return jsonify({"erro:": "operador invalido. Use apenas + - * /"}), 400
        
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
             return jsonify({"erro": "num1 e num2 devem ser numeros"}), 400
        

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                return jsonify({"erro": " divisão por zero não é possivel"}), 400
            resultado = num1 / num2
        
        return jsonify({
            "num1": num1,
            "num2": num2,
            "operador": operador,
            "resultado": resultado
        }), 200
    
    except Exception as e:
        return jsonify({"erro": "dados invalidos"}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
                
