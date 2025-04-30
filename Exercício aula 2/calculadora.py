import math
import os  # Importa o módulo 'os' para limpar a tela

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculadora():
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

    historico = []  # Inicializa a lista para armazenar o histórico

    while True:
        limpar_tela() 
        print("Histórico de Cálculos:")
        if historico:
            for i, item in enumerate(historico): # Exibe o histórico de cálculos
                print(f"{i + 1}. {item}")
        else:
            print("Nenhum cálculo realizado ainda.") # Exibe mensagem se não houver cálculos

        print("\nOperações disponíveis:")
        print("+, -, *, /, ^ (potência), √ (raiz), sen, cos, tan") # Exibe as operações disponíveis
        print("Digite 'sair' para encerrar")

        op = input("Operação: ")

        if op.lower() == 'sair':
            break

        if op in ['√', 'sen', 'cos', 'tan']:
            try:
                num = float(input("Número: "))
                resultado = operacoes[op](num)
                historico.append(f"{op}({num}) = {resultado:.4f}") # Adiciona o cálculo ao histórico
                print(f"Resultado: {resultado:.4f}")
                input("Pressione Enter para continuar...") # Pausa para o usuário ver o resultado
            except ValueError:
                print("Erro: Por favor, digite um número válido.")
                input("Pressione Enter para continuar...")
            except Exception as e:
                print(f"Erro: {e}")
                input("Pressione Enter para continuar...")
        elif op in operacoes:
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))
                resultado = operacoes[op](num1, num2)
                historico.append(f"{num1} {op} {num2} = {resultado:.4f}") 
                print(f"Resultado: {resultado:.4f}")
                input("Pressione Enter para continuar...")
            except ValueError:
                print("Erro: Por favor, digite números válidos.")
                input("Pressione Enter para continuar...")
            except ZeroDivisionError:
                print("Erro: Divisão por zero!")
                input("Pressione Enter para continuar...")
            except Exception as e:
                print(f"Erro: {e}")
                input("Pressione Enter para continuar...")
        else:
            print("Operação inválida!")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    calculadora()