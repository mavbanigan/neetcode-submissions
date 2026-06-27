class Solution:
    def isValid(self, s: str) -> bool:
        # "([{}])" -> input
        # When we turn this string into a stack, it will look like ) -> ] -> } -> { etc.
        if s == []:
            return True
        stack = []
        map = { ')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        return False
                
