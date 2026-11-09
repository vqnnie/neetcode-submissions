class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        each value is being added into the stack until we reach an operator "+-*/"
        then the previous two values will be removed from the stack and the operation
        will be performed and the result will be pushed back onto the stack

        this is a list of str, so we must convert each c to int
        '''

        stack = []

        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                
                elif c == "-": # order matters
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)

                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                
                else: # / operator - order matters
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a)) # must wrap in int to round towards 0

        return stack[-1]