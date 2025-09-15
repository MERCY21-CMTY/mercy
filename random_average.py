import random

def generate_random_numbers(count, start=1, end=100):
    """
    Generate a list of random integers within a specified range.

    Args:
        count (int): Number of random integers to generate.
        start (int): Lower bound of the random range (inclusive).
        end (int): Upper bound of the random range (inclusive).

    Returns:
        list: List of randomly generated integers.
    """
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): List of numbers (int or float).

    Returns:
        float: The average value.
    """
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Generated numbers:", random_numbers)
    avg = calculate_average(random_numbers)
    print("Average:", avg)