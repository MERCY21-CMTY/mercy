def calculate_average(*args):
    if not args:
        return 0

    # The sum() function returns the sum of all items in an iterable.
    # The len() function returns the number of items in an iterable.
    return sum(args) / len(args)
    
#tesing with multiple numbers  
print(f"Average of 5, 10, 15: {calculate_average(5, 10, 15)}")

#testing with a single number
print(f"Average of 42: {calculate_average(42)}")

#testing with floats 
print(f"Average of 1.5, 2.5, 3.0: {calculate_average(1.5, 2.5, 3.0)}")

#testing with  no arguments
print(f"Average with no arguments: {calculate_average()}")
