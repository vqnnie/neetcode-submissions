class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # constraints: i, j, k indices are not equal to each other, no duplicate triplets
        # input: list
        # output: list of lists

        # implementation: two-pointer method, with another pointer i being at the leftmost value
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: # checking that num isn't the same val as its prev num
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result