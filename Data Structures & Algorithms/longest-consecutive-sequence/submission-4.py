class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input: list
        # output: int
        # constraints: no duplicates

        # no sorting, sorting makes it O(nlogn) time

        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet: # find start point, start point don't have left neighbors
            # left neighbors are -1 difference from current num value
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest) # compute max of the previous longest and the length of the current one because if the current 
                                            # length is longer than the previous longest, you want to override that by taking the max
        return longest