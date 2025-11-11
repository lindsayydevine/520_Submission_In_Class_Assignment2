from typing import List, Tuple
import functools

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # If the list is empty, return (0, 1) as per the problem statement
    if not numbers:
        return 0, 1
    # Calculate the sum and product of the list using the built-in functions sum and functools.reduce
    sum_of_numbers = sum(numbers)
    product_of_numbers = functools.reduce(lambda x, y: x * y, numbers)
    return sum_of_numbers, product_of_numbers

# Test the function
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([]))  # Expected output: (0, 1)

# Added automatically for testing
candidate = sum_product
