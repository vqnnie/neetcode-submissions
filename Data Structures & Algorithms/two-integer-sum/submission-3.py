class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution 1: nested loops

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]

        # solution 2: hash map
        # implement using hint 3
        # hint 3 is asking to start with nums[i] and see
        # if the difference exists inside the rest of nums

        # hashmap = set()

        # for i in range(len(nums)):
        #     difference = target - nums[i]

        #     if difference in hashmap:
        #         return [nums.index(difference), i] # use built in index() func
        #     else:
        #         hashmap.add(nums[i])

        # solution 3: hash dict w/ enumerate

        hashmap = {} # mapping value : index, or key : value in dict terms

        for index, value in enumerate(nums):
            difference = target - value

            if difference in hashmap: # check if the difference value exists in hashmap
                return [hashmap[difference], index]
            else:
                hashmap[value] = index