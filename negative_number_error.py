class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is encountered."""
    pass

def check_positive(number):
    """
    Raises NegativeNumberError if the given number is negative.

    Args:
        number (int or float): The number to check.

    Raises:
        NegativeNumberError: If number is negative.
    """
    if number < 0:
        raise NegativeNumberError(f"Negative number encountered: {number}")
    return True