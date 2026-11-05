class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r: # can't be <= because we want to return two indices not one
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
                continue

            if curr_sum < target:
                l += 1

            if curr_sum == target:
                return [l + 1, r + 1]
