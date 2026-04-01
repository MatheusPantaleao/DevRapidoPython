# O projeto foi desenvolvido usando:
# Python – linguagem de programação simples e muito usada no mundo.
# Flask – um microframework que permite criar aplicações web e APIs de forma rápida.

# O sistema cria um pequeno servidor usando Flask.
# Dentro desse servidor existe uma rota chamada: “/calculo” 
# Essa rota recebe uma requisição do tipo POST, contendo três informações:
# num1 → primeiro número e num2 → segundo número e o operador → operação matemática


from flask import Flask, jsonify, request

app = Flask(__name__)

#criando a rota web
@app.route('/calculo', methods=['POST'])
def calculo():
    dados = request.get_json()

    try:
        num1 = dados.get('num1')
        num2 = dados.get('num2')
        operador = dados.get('operador').strip()

        # valida a entrada dos operadores matematicos
        if operador not in ('+', '-', '*', '/'):
            return jsonify({"erro:": "operador invalido. Use apenas + - * /"}), 400
        
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
             return jsonify({"erro": "num1 e num2 devem ser numeros"}), 400
        
        #logica das operaçoes
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
        #retorna com o resultado da operaçao
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
                
# Exemplo de requisição

# Exemplo de dados enviados para a API:

#  “{
#   "num1": 10,
#   "num2": 5,
#   "operador": "+"
#   }” - código 
