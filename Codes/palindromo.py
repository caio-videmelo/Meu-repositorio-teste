def is_palindrome(word):
    """
    Check if a word or phrase is a palindrome.
    
    Parameters:
    word (str): The word or phrase to check.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Reverse the word
    reversed_word = word[::-1]
    # Compare the original word with the reversed word
    return word == reversed_word

def main():
    """
    Main function to execute the palindrome check.
    """
    # Request input from the user
    user_input = input("Digite uma palavra ou frase: ")

    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" é um palíndromo.')
    else:
        print(f'"{user_input}" não é um palíndromo.')

if __name__ == "__main__":
    main()
