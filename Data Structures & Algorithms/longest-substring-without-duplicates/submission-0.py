class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        - UNDERSTAND
        input: str
        output: int

        edge case: no duplicate, as soon as you encounter a duplicate substring, stop adding to count

        - PLAN
        set contains unique char, no duplicates
        two pointer for sliding window
        l - start of window
        r - end of window, visits every char

        initialize set() and l pointer
        for loop iterates through str
            while duplicate is inside set, 
                remove leftmost val and increment l pointer until duplicate is gone
            when duplicate is removed, add new val s[r]
        result is updated to max of prev result and new result, result = r - l + 1
        result needs to +1 to include val not just the val in between the l and r pointers

        when you encounter a duplicate, calculate diff in substring length, set l at that location
        '''

        charSet = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res