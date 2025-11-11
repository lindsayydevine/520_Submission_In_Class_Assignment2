Here is an example of what the code should look like:

                    def rolling\_max(numbers: List[int]) -> List[int]:
                        """ From a given list of integers, generate a list of rolling maximum element found until given moment
                        in the sequence.
                        
                        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
                        [1, 2, 3, 3, 3, 4, 4]
                        """

                        if not numbers:
                            return []

                        result = [numbers[0]]

                        for i in range(1, len(numbers)):
                            if numbers[i] > result[-1]:
                                result.append(numbers[i])
                            else:
                                result.append(result[-1])

                        return result

                    # Example usage:
                    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))

                    
                    If the above code

# Added automatically for testing
candidate = rolling_max
