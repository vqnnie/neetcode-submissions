class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution 1: nested loops

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

        # solution 2: hash map
        # implement using hint 3
        # hint 3 is asking to start with nums[i] and see
        # if the difference exists inside the rest of nums

        hashmap = set()

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in hashmap:
                break
            else:
                hashmap.add(nums[i])

        return [i, nums.index(difference)] # use built in index() func
        