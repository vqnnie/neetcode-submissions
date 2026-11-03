class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # note: 1 indexed list

        l, r = 0, len(numbers) - 1 # l starts at 0 regardless of whether it's a 0 or 1

        while l < r:
            if numbers [l] + numbers[r] == target:
                break
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]