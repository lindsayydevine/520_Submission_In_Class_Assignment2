Your solution should parse the input string to count the number of opening and closing parentheses,
                    and then return the maximum count of opening parentheses at any level of nesting.
                    To solve this problem, you can use recursion.
                    Start by defining the `parse_nested_parens` function.
                    
                    Example usage:
                    >>> parse_nested_parens('(()()) ((())) () ((())()())')
                    [2, 3, 1, 3]
                    
                    Hint:
                    You can use a variable to keep track of the maximum number of opening parentheses at each level.
                    Initialize this variable to 0, and update it when you encounter an opening parenthesis at a deeper level.
                    Return this variable when you encounter a closing parenthesis.
                    
                    You can use a list to store all opening parenthesis counts at each level, and return this list when you encounter a closing parenthesis.
                    
                    Test your solution with the example input provided above.


                    """

                    # Solution

                    def parse

# Added automatically for testing
candidate = parse_nested_parens
