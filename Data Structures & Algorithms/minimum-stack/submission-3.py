class MinStack:
    '''
    our goal is to support all operations in constant O(1) time
    to achieve this, we create two stacks: regular stack where we push each element to and minimum stack that assigns the minimum value to each element in the regular stack

    things to keep in mind:
    - when you push a val, you push a val to both stack and min_stack
    - when you pop a val, you pop the topmost element of both stacks
    - when you get the top val, we return the top of the first stack
    - when you get the min val, we return the top of the min_stack 
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if there is already a val in min_stack
        # append the min of the top value from min_stack vs the val we are pushing
        if self.min_stack:
            val = min(self.min_stack[-1], val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]