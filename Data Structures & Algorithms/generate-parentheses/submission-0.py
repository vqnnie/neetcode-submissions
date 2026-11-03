class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # input: int
        # output: list of size 2n strings

       # only add open parenthesis if open < n
       # only add closing parenthesis if closed < open
       # valid IFF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # when a return is reached, pop one open (
                # stack.pop() removes the last element, one parenthesis, from the stack

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # when a return is reached, pop one closed (

        backtrack(0, 0)
        return res