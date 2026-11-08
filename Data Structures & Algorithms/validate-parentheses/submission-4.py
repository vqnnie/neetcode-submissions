class Solution:
    def isValid(self, s: str) -> bool:
        '''
        simplified code without all the comments

        i find that i need to visualize this to truly understand the code, so next time i will draw this out
        '''

        # an empty s is valid, so don't return False if s is empty

        stack = [] # stores opening brackets that haven't been matched yet
        close_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        return False