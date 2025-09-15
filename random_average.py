import random

def generate_random_numbers(count, start=1, end=100):
   
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
  
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    random_numbers = generate_random_numbers(10, 1, 100)
    print("Generated numbers:", random_numbers)
    avg = calculate_average(random_numbers)
    print("Average:", avg)
