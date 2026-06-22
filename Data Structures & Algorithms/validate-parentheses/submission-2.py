class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Initializing Stack
        map = { ")" : "(", "]" : "[", "}" : "{"} # Mapping Open to Close brackets
        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

        