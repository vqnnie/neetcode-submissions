class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1: brute force
        new_s = ""

        for c in s:
            if c.isalpha() or c.isdigit(): # checks for only a-z and 0-9
                new_s += c
        reversed_s = new_s[::-1]

        if new_s.lower() == reversed_s.lower():
            return True
        return False