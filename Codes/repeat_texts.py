def repeat_text(text, number):
    """
    Repeat the given text a specified number of times, separated by spaces.
    
    Parameters:
    text (str): The text to repeat.
    number (int): The number of times to repeat the text.

    Returns:
    str: The repeated text.
    """
    return (text + ' ') * number

def main():
    """
    Main function to execute the text repetition.
    """
    # Request input from the user
    text = input("Digite uma string: ")
    number = int(input("Digite um número inteiro: "))

    # Print the repeated text
    print(repeat_text(text, number))

if __name__ == "__main__":
    main()
