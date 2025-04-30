from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def calcular(operacao, num1=None, num2=None):
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y,
        '√': lambda x: math.sqrt(x),
        'sen': lambda x: math.sin(math.radians(x)),
        'cos': lambda x: math.cos(math.radians(x)),
        'tan': lambda x: math.tan(math.radians(x))
    }
    try:
        if operacao in ['√', 'sen', 'cos', 'tan']:
            return operacoes[operacao](num1)
        elif operacao in operacoes:
            return operacoes[operacao](num1, num2)
        else:
            return "Operação inválida!"
    except ZeroDivisionError:
        return "Erro: Divisão por zero!"
    except ValueError as e:
        return f"Erro: {e}"
    except Exception as e:
        return f"Erro: {e}"

@app.route('/', methods=['GET'])
def index():
    return render_template('calculadora.html')

@app.route('/calcular', methods=['POST'])
def calcular_rota():
    data = request.form
    operacao = data.get('operacao')
    num1 = data.get('num1')
    num2 = data.get('num2')

    try:
        if num1 is not None:
            num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)
        resultado = calcular(operacao, num1, num2)
        return jsonify({'resultado': f"{resultado:.4f}"})
    except ValueError:
        return jsonify({'erro': 'Entrada inválida!'})

if __name__ == '__main__':
    app.run(debug=True)