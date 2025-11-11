def rolling_max(numbers: List[int]) -> List[int]:
    max_list = []
    current_max = None
    for number in numbers:
        if current_max is None:
            max_list.append(number)
            current_max = number
        else:
            if number > current_max:
                max_list.append(number)
                current_max = number
            else:
                max_list.append(current_max)
    return max_list

candidate = rolling_max
