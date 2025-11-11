def has\_close\_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    
    Args:
    numbers: List of float numbers
    threshold: Threshold value for closeness
    
    Returns:
    bool: True if any two numbers are closer to each other than threshold, False otherwise
    """
    # Check if list has at least 2 elements
    if len(numbers) < 2:
        return False
    # Initialize variables
    count = 0
    # Iterate through the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Check if two numbers are closer to each other than threshold
            if abs(numbers[i] - numbers[j]) < threshold:
                count += 1
    # Return result
    return count > 0


###

Problem 11
=========


def longest\_streak(numbers: List[float]) -> float:


candidate = has_close_elements
