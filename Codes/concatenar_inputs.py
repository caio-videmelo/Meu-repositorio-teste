def main():
    """
    This function receives two inputs from the user and concatenates them.
    """
    # Receive two different pieces of information from the user
    info1 = input("Digite a primeira informação: ")
    info2 = input("Digite a segunda informação: ")

    # Concatenate the inputs with a space in between
    concatenated_info = f"{info1} {info2}"

    # Print the concatenated information
    print("As informações concatenadas são:", concatenated_info)

if __name__ == "__main__":
    main()
