from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    groups = []
    open_count = 0
    for c in paren_string:
        if c == '(':
            open_count += 1
            groups.append(c)
        elif c == ')':
            open_count -= 1
            if open_count == 0:
                result.append(''.join(groups))
                groups = []
        else:
            continue
    return result

# Added automatically for testing
candidate = separate_paren_groups
