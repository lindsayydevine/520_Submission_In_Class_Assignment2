import typing


def intersperse(numbers: typing.List[int], delimeter: int) -> typing.List[int]:
    result: typing.List[int] = []
    for i in numbers:
        result.append(i)
        if i!= numbers[-1]:
            result.append(delimeter)
    return result

# Added automatically for testing
candidate = intersperse
