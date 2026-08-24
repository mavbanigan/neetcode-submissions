class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # Lowercase
        Ls = []
        for char in s:
            if char.isalnum() == True: # Check for non-alphanumeric chars
                Ls.append(char)
        i = 0 # First pointer
        j = len(Ls)-1 # Second pointer
        while i <= j:
            if Ls[i] != Ls[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        
                

        