from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    for group in groups:
        max_depth = 0
        depth = 1
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        result.append(max_depth)
    return result

# Added automatically for testing
candidate = parse_nested_parens
