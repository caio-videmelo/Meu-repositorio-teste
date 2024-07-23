# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

# Vamos solicitar ao usuário que escolha a operação a ser realizada:
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Inicializamos a variável resultado
resultado = None

# Operações com os números inseridos pelo usuário:
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = abs(num1 - num2)
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:  # Verificamos se o divisor não é zero
        resultado = num1 / num2
    else:
        resultado = "Indefinido (divisão por zero)"
else:
    resultado = "Operação inválida"

# Apresentar os resultados:
print("O resultado da operação é: ", resultado)
