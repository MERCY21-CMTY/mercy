def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")

print(divide_numbers(20, 2))    
print(divide_numbers(20, 0))    
print(divide_numbers("20", 2))  
