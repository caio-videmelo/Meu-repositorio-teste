def perform_operation(num1, num2, operation):
    """
    Perform a simple arithmetic operation between two numbers.
    
    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    operation (str): The operation to perform ('+', '-', '*', '/').

    Returns:
    result: The result of the operation, or a string indicating an invalid operation or division by zero.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return abs(num1 - num2)
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else "Indefinido (divisão por zero)"
    else:
        return "Operação inválida"

def main():
    """
    Main function to execute the arithmetic operations.
    """
    # Request input from the user
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))

    # Request the operation from the user
    operation = input("Digite a operação que deseja realizar (+, -, *, /): ")

    # Perform the operation and store the result
    result = perform_operation(num1, num2, operation)

    # Display the result
    print("O resultado da operação é:", result)

if __name__ == "__main__":
    main()
