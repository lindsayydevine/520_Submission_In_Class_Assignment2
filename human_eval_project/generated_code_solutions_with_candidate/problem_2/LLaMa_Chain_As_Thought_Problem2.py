import re
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is
    to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # First, remove any spaces in the string
    paren_string = paren_string.replace(' ', '')

    # Then, use a regular expression to find all balanced groups of parentheses
    groups = re.findall(r'\([^()]*\)', paren_string)

    # Finally, return the list of groups
    return groups

# Added automatically for testing
candidate = separate_paren_groups
