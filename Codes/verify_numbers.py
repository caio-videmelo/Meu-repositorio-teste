def check_even_odd(number):
    """
    Check if a number is even or odd.
    
    Parameters:
    number (int): The number to check.

    Returns:
    str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"O número {number} é par."
    else:
        return f"O número {number} é ímpar."

def main():
    """
    Main function to execute the even or odd check.
    """
    # Request input from the user
    num = int(input("Digite um número inteiro: "))

    # Check if the number is even or odd and display the result
    result = check_even_odd(num)
    print(result)

if __name__ == "__main__":
    main()
