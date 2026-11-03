class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1: brute force
        # new_s = ""

        # for c in s:
        #     if c.isalnum(): # checks for only a-z and 0-9
        #         new_s += c

        # return new_s.lower() == new_s[::-1].lower()

        # solution 2: two pointer, O(1) space

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]): # to call another function inside the same object, you need to use self.
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -=1
        return True

    def alphaNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9"))
