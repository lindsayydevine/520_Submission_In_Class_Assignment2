def mean_absolute_deviation(numbers: List[float]) -> float:
        """
        Calculate the mean absolute deviation of a list of numbers.

        Parameters:
        numbers (List[float]): A list of numbers.

        Returns:
        float: The mean absolute deviation of the input numbers.

        Example:
        mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        Output:
        1.0
        """
        if not numbers:
            raise ValueError("List of numbers cannot be empty.")

        # Calculate the mean of the input numbers
        mean = sum(numbers) / len(numbers)

        # Calculate the absolute deviations from the mean
        absolute_deviations = [abs(x - mean) for x in numbers]

        # Calculate the sum of the absolute deviations
        sum_of_absolute_deviations = sum(absolute_deviations)

        # Calculate the mean absolute deviation
        mad = sum_of_absolute_deviations / len(numbers

# Added automatically for testing
candidate = mean_absolute_deviation
