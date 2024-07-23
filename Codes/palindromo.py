# Função para verificar se uma palavra é um palíndromo
def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Inverte a palavra
    palavra_invertida = palavra[::-1]
    # Compara a palavra original com a invertida
    return palavra == palavra_invertida

# Solicita a palavra ao usuário
entrada = input("Digite uma palavra ou frase: ")

# Verifica se a entrada é um palíndromo
if eh_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')
