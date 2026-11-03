class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # implement using nested loops w var i and j

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # implement using hash set

        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False