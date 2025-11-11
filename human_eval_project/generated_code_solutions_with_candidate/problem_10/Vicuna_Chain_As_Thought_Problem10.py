This function takes a list of integers as input and returns a new list of integers, which is the
                    list of the maximum elements in the original list, up to the given index in the original list.
                    The function uses a for loop to iterate through the original list and a while loop to find the
                    maximum element up to the given index. The while loop continues until the maximum element is found
                    or the index is greater than the length of the original list. The maximum element is added to a new
                    list, which is returned as the output.
                    """

                    def rolling_max(numbers: List[int]) -> List[int]:
                        if len(numbers) == 0:
                            return []
                        else:
                            result = [numbers[0]]
                            for i in range(1, len(numbers)):
                                while numbers[i] < numbers[i - 1]:
                                    numbers[i - 1] = numbers[i - 2]
                                result.append(numbers[i])
                            return result

                    # Check if the function works

# Added automatically for testing
candidate = rolling_max
