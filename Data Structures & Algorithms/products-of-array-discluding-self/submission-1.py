class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix) # we want to store the prefix of each num in the res array
            prefix *= nums[i] # prefix gets updated and multiplied by nums[i], which becomes the prefix for the next num

        postfix = 1 # now we find postfix starting from end of array
        for i in range(len(nums) - 1, -1, -1): # reminder that this excludes -1 so it includes 0
            # multiply res[i], which ressembles the prefix, by postfix
            res[i] *= postfix
            postfix *= nums[i]

        return res