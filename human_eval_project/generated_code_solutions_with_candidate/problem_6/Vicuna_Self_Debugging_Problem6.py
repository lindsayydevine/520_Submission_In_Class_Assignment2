def intersperse(numbers: List[int], delimeter: int) -> List[int]:
                        """
                        Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
                        """
                        result = []
                        for i in range(0, len(numbers), 2):
                            if i % 2 == 0:
                                result.append(numbers[i])
                            else:
                                result.append(delimeter)
                            result.append(numbers[i + 1])
                        return result
                    
                    # Test the function with the given examples
                    print(intersperse([], 4))
                    print(intersperse([1, 2, 3], 4))


Example:

intersperse([1, 2, 3], 4)
Output: [1, 4, 2, 4, 3]

intersperse([], 4)
Output: []

Your code should pass all the given tests. Try to write a clean and

# Added automatically for testing
candidate = intersperse
