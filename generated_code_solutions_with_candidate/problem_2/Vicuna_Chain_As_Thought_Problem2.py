Here is a possible solution:
                    
                    You can use a stack to keep track of open parentheses.
                    
                    Initially, the stack is empty.
                    
                    You iterate through the input string, one character at a time.
                    
                    If the character is an open parenthesis, you push it onto the stack.
                    
                    If the character is a close parenthesis, you pop the stack until you find an open parenthesis that matches the close parenthesis.
                    
                    If the stack becomes empty, it means that we have reached the end of a group of parentheses.
                    
                    You can then add the characters in the group to a list and return that list.
                    
                    Here is a possible implementation of the above solution:
                    
                    def separate_paren_groups(paren_string: str) -> List[str]:
                        groups = []
                        stack = []
                        for char in paren_string:
                            if char == '(':
                                stack.append(char)
                            else:

# Added automatically for testing
candidate = separate_paren_groups
