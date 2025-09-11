def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def get_integer_input(prompt="Enter an integer: "):
    while True:
        user_input = input(prompt)
        try:
            num = int(user_input)
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    num = get_integer_input()
    result = classify_number(num)
    print(f"The number is {result}.")