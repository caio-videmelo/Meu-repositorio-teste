def calculate_mean_grade():
    """
    This function calculates the mean of three grades provided by the user.
    """
    # Request grades from the user
    grade1 = float(input("Digite a primeira nota: "))
    grade2 = float(input("Digite a segunda nota: "))
    grade3 = float(input("Digite a terceira nota: "))

    # Calculate the mean
    mean_grade = (grade1 + grade2 + grade3) / 3

    # Display the result
    print(f"A média das notas é: {mean_grade:.2f}")

if __name__ == "__main__":
    calculate_mean_grade()
