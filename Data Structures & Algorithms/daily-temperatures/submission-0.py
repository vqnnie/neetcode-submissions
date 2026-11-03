class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        UNDERSTAND:
        input: list
        output: list

        idea: list returns the number of days it takes until
        temperatures[j] > temperatures[i], therfore returning j - 1
        j is the temp higher than the temp at i

        edge cases: no temperature higher than temperatures[i], return 0
        at that index

        this is a montonically decreasing stack, meaning all elements are in
        decreasing order, with the top value the greatest value

        use enumerate() to track val and index

        PLAN:
        initialize stack, res
        compare stack.pop() < temperatures[i]
        if true, subtract temperatures i by stack[-1] index from temperatures, append to res in corresponding pos of stack.pop()
        stack.pop() happens simulataneously, so last element will also be removed from stack
        else, stack.append(temperaturess[i])

        '''

        stack = [] # store val and index - pair: [temp, index]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: # top val is at index 0 b/c this is montonically dec stack
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex # add difference between i in temperature and i of value in stack
            stack.append([temp, i])
        return res