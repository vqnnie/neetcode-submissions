class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        - UNDERSTAND
        input: list of int
        output: int

        two pointer algorithm
        trapped water at index i: min(height[l], height[r]) - height[i]

        - CALCULATIONS
        water at index i, maxLeft height, maxRight height, min(height[l], height[r])
        
        - PLAN
        l, r = 0, len(height) - 1
        maxL = max(maxL, height[l])
        maxR = max(maxL, height[r])

        shift the pointer that is the min of maxL or maxR
        for ex, if maxR < maxL, shift r pointer and vice versa
        '''

        # Edge case
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res