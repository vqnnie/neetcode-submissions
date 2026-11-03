class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        - UNDERSTAND
        input: int, list, list
        output: int

        since it is a one-lane road, cars starting w/ diff speeds are
        bound to travel at the same speed, the slower speed, behind them
        creating a car fleet 

        cars next to each other are assumed to have the same position
        (distance between two cars are ignored)

        - PLAN
        initialize a stack
        sort pair list of (position, speed)
        retrieve last two (greatest position) cars in list
        if they collide, remove the top of the stack using stack.pop()
        '''

        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: # reverse sorted order
            stack.append((target - p) / s) # calculate time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # this means that a car joins a fleet
        return len(stack) # returns all the individual, DIFFERENT car fleets