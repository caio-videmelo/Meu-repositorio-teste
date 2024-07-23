# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.
# Solicitar ao usuário que insira um número inteiro
num = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar usando um valor booleano
is_even = (num % 2 == 0)

# Apresentar o resultado
if is_even:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")
