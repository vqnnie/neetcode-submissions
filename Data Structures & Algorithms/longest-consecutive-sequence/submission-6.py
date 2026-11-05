class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we use a set instead of keeping it as an array for faster lookups (better big O)
        nums_set = set(nums)
        longest = 0
        # length can't be initiated outside of the loop because length = 0 determines the start value

        for n in nums:
            # check if there is a left neighbor, if there is then n is not a start value. skip this n and move to the next n.
            if (n - 1) in nums_set:
                continue
            length = 0
            while (n + length) in nums_set: # iterate through array, starting with start value (n + 0)
                length += 1
            longest = max(length, longest) # finds max between current longest value and length in case length is the longest consec sequence
        return longest