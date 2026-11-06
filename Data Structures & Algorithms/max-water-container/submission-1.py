class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        TWO POINTERS ALGORITHM

        linear time solution: O(n)

        important notes:
        - the container is limited by the shortest bar (the minimum value) the container can not be higher than the shortest bar. so our bottleneck is the minimum bar value.
        - width is the difference between the l and r pointers
        - height of the max container is determined by the minimum height value (minimum of the two bar values)

        area = width x height

        '''

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            # this is important:
            # you must use r - l and not l - r because r > l and l - r will always result in a negative value and will return max_area = 0 because 0 is greater than a negative value
            area = (r - l) * min(heights[l], heights[r]) # find the minimum value between the value at l and the value at r, i.e. find the minimum height
            max_area = max(area, max_area)
            
            # we want to maximize our area now, so we are going to move our pointers
            # move the pointer that has the smaller height value
            if heights[l] < heights[r]:
                l += 1 # heights[l] is smaller so move the pointer to the right
            else:
                r -= 1

        return max_area