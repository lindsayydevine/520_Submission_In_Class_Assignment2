from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        current_max = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j] > current_max:
                current_max = numbers[j]
        result.append(current_max)
    return result

candidate = rolling_max
