from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Iterate over the list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            # If it is, return True
            return True
    # If the loop completes without finding two numbers that are closer than the threshold, return False
    return False

candidate = has_close_elements
