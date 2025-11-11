# Your code here
                    pass

                    # Solution
                    def filter_by_substring(strings: List[str], substring: str) -> List[str]:
                        filtered_strings = []
                        for s in strings:
                            if substring in s:
                                filtered_strings.append(s)
                        return filtered_strings

                    # Test cases
                    test_case_1 = ([], 'a')
                    test_case_2 = (['abc', 'bacd', 'cde', 'array'], 'a')

                    # Check if function passes all test cases
                    assert filter_by_substring(test_case_1[0], test_case_1[1]) == test_case_1[2]
                    assert filter_by_substring(test_case_2[0], test_case_2[1]) == test_case_2[2]

# Added automatically for testing
candidate = filter_by_substring