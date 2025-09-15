def get_valid_number():
    
    while True:
        user_input = input("9: ")
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("21.")

if __name__ == "__main__":
    number = get_valid_number()
    print(f"21: {number}")
