def below_zero(operations: List[int]) -> bool:
        """
        Determines if the balance of the bank account falls below zero at any point during the given operations.
        
        Args:
            operations: List[int] - A list of deposit and withdrawal operations to be performed on a bank account.
        
        Returns:
            bool - True if the balance falls below zero at any point, False otherwise.
            
        Example:
            below_zero([1, 2, 3]) returns False because the balance never falls below zero.
            below_zero([1, 2, -4, 5]) returns True because the balance falls below zero after the third operation.
        """
        
        # Initialize the balance to zero
        balance = 0
        
        # Iterate through the operations
        for operation in operations:
            # Determine if the operation is a deposit or withdrawal
            if operation > 0:
                # Deposit
                balance += operation
            else:
                # Withdrawal
                balance -= operation
                
            # Check if the balance is

# Added automatically for testing
candidate = below_zero
