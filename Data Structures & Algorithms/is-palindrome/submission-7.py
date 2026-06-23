class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer question, l = 0, r = len(s)-1. 
        # Need to ignore spaces and non-alphanumeric characters
        l = 0
        r = len(s)-1
        # Loops until the left and right meet in the middle
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
