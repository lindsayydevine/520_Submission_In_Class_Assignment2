import math


def truncate_number(number: float) -> float:
    # Get the integer part of the number
    integer_part = math.floor(number)
    # Get the decimal part of the number
    decimal_part = number - integer_part
    return decimal_part

# Added automatically for testing
candidate = truncate_number
