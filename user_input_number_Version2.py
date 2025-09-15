def get_valid_number():
    """
    Prompt the user to enter a valid number. If the input is not a valid number,
    catch the ValueError and prompt again until a valid number is entered.

    Returns:
        float: The valid number entered by the user.
    """
    while True:
        user_input = input("9: ")
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("21.")

# Example usage:
if __name__ == "__main__":
    number = get_valid_number()
    print(f"You entered: {number}")