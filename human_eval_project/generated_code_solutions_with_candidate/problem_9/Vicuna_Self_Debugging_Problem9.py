def sum\_product(numbers: List[int]) -> Tuple[int, int]:
                        """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
                        Empty sum should be equal to 0 and empty product should be equal to 1.
                        >>> sum\_product([])
                        (0, 1)
                        >>> sum\_product([1, 2, 3, 4])
                        (10, 24)
                        """
                        if not numbers:
                            return 0, 1
                        else:
                            sum = numbers[0]
                            product = 1
                            for num in numbers[1:]:
                                sum += num
                                product *= num
                            return sum, product
                    
                    # Test the function
                    print(sum_product([1, 2, 3, 4])) # expected output: (10, 24)
                    print(sum_product([0, -1, 2, -3])) #

# Added automatically for testing
candidate = sum_product
