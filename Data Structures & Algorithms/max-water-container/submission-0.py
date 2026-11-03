class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # input: list
        # output: int
        # constraints: need to use min height or else water can leak
        # goal: find the max area, with max width and second max height
        # two pointer algorithm

        result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result