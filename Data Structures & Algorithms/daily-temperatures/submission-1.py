class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        >> monotonic decreasing order stack problem <<

        keep track of where the indices and use the indices to determine differences
        
        - compare the temp to the top of the stack
        - if greater, we pop the top of the stack
        - when we find a higher temp, we pop the previous 
        - if the current temp is lower than the top of the stack, push current temp to stack

        stack[-1][0] gets the top pair’s temperature.
        stack[-1][1] gets the top pair’s original day index.

        implementation:
        - while stack is not empty and current temp is greater than top of the stack, keep popping the top of the stack until current temp is less than top of the stack
        - when current temp is less than top of the stack, add current temp to the stack
        '''

        stack = [] # pair: [temp, index]
        res = [0] * len(temperatures) # sets output representing number of days to 0 by default

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # stack[-1][0] retrieves top pair's temp
                top_temp, top_index = stack.pop()
                res[top_index] = i - top_index
            stack.append([temp, i]) 
        return res
