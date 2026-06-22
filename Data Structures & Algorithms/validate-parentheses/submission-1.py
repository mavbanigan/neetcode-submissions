class Solution:
    def isValid(self, s: str) -> bool:
        Stack = [] # Initializing Stack
        Map = { ")" : "(", "]" : "[", "}" : "{"} # Mapping Open to Close brackets
        for char in s:
            if char in Map:
                if Stack and Stack[-1] == Map[char]:
                    Stack.pop()
                else:
                    return False
            else:
                Stack.append(char)
        return len(Stack) == 0

        