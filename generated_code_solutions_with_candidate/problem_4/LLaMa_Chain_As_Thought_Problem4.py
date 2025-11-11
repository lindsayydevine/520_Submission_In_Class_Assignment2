from typing import List


def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    The function will iterate over the list of operations, and for each operation, it will add the operation
    to the previous balance. If at any point the balance is less than zero, it will return True. Otherwise
    it will return False.
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False

# Added automatically for testing
candidate = below_zero
