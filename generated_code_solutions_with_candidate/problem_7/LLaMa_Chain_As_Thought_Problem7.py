import re
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = re.split(r'\s+', paren_string)
    max_nesting = []
    for group in groups:
        nesting = 1
        max_nesting.append(nesting)
        for paren in group:
            if paren == '(':
                nesting += 1
            else:
                nesting -= 1
    return max_nesting

# Added automatically for testing
candidate = parse_nested_parens
