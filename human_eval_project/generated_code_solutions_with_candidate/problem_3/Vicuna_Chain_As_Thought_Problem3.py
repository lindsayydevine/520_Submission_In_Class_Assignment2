def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into an integer part
    (largest integer smaller than given number) and decimals (leftover part always
    smaller than 1). Return the decimal part of the number.

    :param number: The positive floating point number to be truncated.
    :return: The decimal part of the given number.
    """

    # Step 1: Convert the input number to a string.
    number_str = str(number)

    # Step 2: Extract the integer part by removing the decimal part.
    integer_part = int(number_str)

    # Step 3: Remove the integer part from the original number_str.
    decimal_part = float(number_str - str(integer_part))

    # Step 4: Return the decimal part.
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Output: 0.5

# Added automatically for testing
candidate = truncate_number
