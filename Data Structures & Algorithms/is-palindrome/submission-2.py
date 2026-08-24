class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2 = ""
        for char in s:
            if char.isalnum():
                str2 += char.lower()
        return str2 == str2[::-1]
                

        