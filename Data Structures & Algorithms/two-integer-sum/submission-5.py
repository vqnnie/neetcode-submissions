class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        from what i recall, this has something to do with calculating the difference
        
        make sure i != j
        return answer with smaller index first

        brute force solution first

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    if i < j: return [i, j]
                    else: return [j, i]

        # what happens if nums is an empty list?
        '''

        '''
        my next approach is find difference = target - nums[i] and see if difference exists in the nums list and return true if it exists
        '''

        hashmap = {}
        # we want to map value : index

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i