import typing

def intersperse(numbers: typing.List[int], delimeter: int) -> typing.List[int]:
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    return result

# Added automatically for testing
candidate = intersperse
