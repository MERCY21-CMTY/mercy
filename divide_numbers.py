def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")

# Example usage:
print(divide_numbers(10, 2))    # Output: 5.0
print(divide_numbers(10, 0))    # Error: Division by zero is not allowed.
print(divide_numbers("10", 2))  # Error: Both numerator and denominator must be numbers.