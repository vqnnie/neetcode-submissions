class Solution:
    def isValid(self, s: str) -> bool:
        '''
        stack operations:
        stack.append()
        stack.pop()
        stack[-1] <= "peek"

        things to keep in mind:
        - matching an open bracket with its corresponding bracket
        - 
        '''
        stack = []
        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        if not s:
            return False

        for c in s:
            # push opening brackets onto stack
            if c in "({[":
                stack.append(c)
            # check if stack is non-empty and if c is the closing bracket to the last element in stack
            elif stack and close_to_open[c] == stack[-1]:
                stack.pop()
            # if the above are false (i.e. the closing parentheses don't match with an opening), return false
            else:
                return False
        # this is very important
        # if the stack is empty, then all the opening parentheses have a closing parenthese and vice versa
        # if the stack is not empty, then there's an opening parenthese that doesn't have a closing parenthese
        if not stack:
            return True
        return False