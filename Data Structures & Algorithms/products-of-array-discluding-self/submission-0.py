class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix method, traversing the list twice
        # prefix traverse: left to right
        # postfix traverse: right to left

        # default prefix at index 0 is 1, default postfix at index len(nums) is 1

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # how to iterate starting from end to beginning
                                               # len(nums) - 1 start point, includes num there
                                               # -1 end point goes up to but not including -1, we want it to reach 0, so we choose -1
            res[i] *= postfix
            postfix *= nums[i]

        return res