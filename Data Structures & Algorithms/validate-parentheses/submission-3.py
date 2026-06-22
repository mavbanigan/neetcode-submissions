class Solution:
    def isValid(self, s: str) -> bool:
        
        # It's good to remember that we're only ever pushing open brackets to the stack.
        # This is so we can check if each open bracket in the stack corresponds to their
        # respective closed bracket in the hashmap, via popping from the stack.

        stack = [] # Initializing Stack
        map = { ")" : "(", "]" : "[", "}" : "{"} # Mapping Close to Open brackets
        # Check every bracket in the string
        for char in s:
            # If it's a closed bracket
            if char in map:
                # If the stack isn't empty, and the top of the stack maps to its corresponding closed bracket
                if stack and stack[-1] == map[char]:
                    # Pop the bracket, so we don't have to check it anymore
                    stack.pop()
                else:
                    return False
            else:
                # Push the open bracket onto the stack
                stack.append(char)
        # Return True if the stack has been emptied out
        return len(stack) == 0