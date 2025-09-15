def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.
    
    Args:
        *args: A variable-length argument list of numbers (int or float).
        
    Returns:
        float: The average value of the provided numbers.
        
    Raises:
        ValueError: If no arguments are provided.
        
    Example:
        >>> calculate_average(1, 2, 3, 4)
        2.5
    """
    if not args:
        raise ValueError("At least one number must be provided")
    return sum(args) / len(args)