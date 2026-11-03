class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack: return False # if there are no opening brackets, return False instantly
                top = stack[-1]
                if (char == ")" and top != "(") or (char == "]" and top != "[") or (char == "}" and top != "{"):
                    return False
                stack.pop() # pop opening bracket if opening bracket match
        return not stack