class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        input: nums
        output: boolean (true/false)

        brute force solution first

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]: return True
        return False
        '''
        '''
        keyword - "duplicates" -> hashmap/hashtable/dict
        '''

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
