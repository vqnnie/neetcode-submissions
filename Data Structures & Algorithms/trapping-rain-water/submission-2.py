class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        TWO POINTERS METHOD

        edge case: if the list is empty, return 0
        
        implementation:
        there will be 2 pointers: l and r. we use l or r depending on whether max left or max right is smaller. then we increment l or decrement r and update the max with the current height value if it is greater than the already max value. then we calculate the amount of water being trapped by subtracting the max left/right by the current height.

        essentially the amount of water is being determined by finding the smaller height of the left or right bar of the current height we are at. but we first track the max left and right bars and then find the smaller max to subtract by the current height. 

        '''

        # edge case
        if not height:
            return 0

        water = 0
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(height[l], left_max)
                water += left_max - height[l]
            else:
                r -= 1
                right_max = max(height[r], right_max)
                water += right_max - height[r]
        return water