This problem can be solved by using a list comprehension and the `in` keyword.
                    The list comprehension will iterate over the input list and check if the substring is in the string.
                    If the substring is in the string, it will be added to the output list.

                    Here is the full working function:

                    def filter_by_substring(strings: List[str], substring: str) -> List[str]:
                        """ Filter an input list of strings only for ones that contain given substring

                        Args:
                            strings: List of strings to filter
                            substring: Substring to search for

                        Returns:
                            List of strings that contain the given substring

                        Example:
                            filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
                        """

                        return [string for string in strings if substring in string]

                    # Test the function with the examples in the problem prompt
                    filter_by_substring([], 'a')
                    filter_by_substring(['abc', 'bac
                                         
# Added automatically for testing
candidate = filter_by_substring                                        