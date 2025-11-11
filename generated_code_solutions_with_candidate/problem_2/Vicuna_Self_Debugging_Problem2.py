# Example of valid input string
                    example_input_string = '( ) (( )) (( )( ))'
                    
                    # Initialize empty list to store the separated strings
                    separated_strings = []
                    
                    # Initialize variable to store the current open parenthesis count
                    current_open_paren_count = 0
                    
                    # Loop through the input string
                    for char in paren_string:
                        # If the current character is an open parenthesis
                        if char == '(':
                            # Increment the current open parenthesis count
                            current_open_paren_count += 1
                        # If the current character is a closing parenthesis
                        elif char == ')':
                            # Decrement the current open parenthesis count
                            current_open_paren_count -= 1
                            
                            # If the current open parenthesis count becomes 0
                            if current_open_paren_count == 0:
                                # Add the current substring to the separated strings list

# Added automatically for testing
candidate = separate_paren_groups
