class Solution:

    def encode(self, strs: List[str]) -> str:
        # input: list of strings [..., ..., ...]
        # output: string

        # example:
        # Input: ["neet","code","love","you"]
        # Output:["neet","code","love","you"]

        # step 1: start w/ a number representing the length of the string
        # step 2: follow w/ a delimiter, e.g. #
        # step 3: then grab that many characters for the string

        result = []
        for s in strs:
            result.append(str(len(s)) + "#" + s)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        # input: string
        # output: list of strings

        # using pointers, i used for start point of the length of the string
        # j used for keeping track of length of string

        result = []
        i = 0 # index 0 always is an int

        while i < len(s):
            j = i # j also starts at index 0
            while s[j] != "#":
                j += 1 # j pointer moves 1 index to the right until # is reached
                       # this accounts for an edge case where there is more than 1 digit strings
            length = int(s[i : j]) # length of one str inside s, not including j, the #
            result.append(s[j + 1 : j + 1 + length]) # j + 1 skips the #, j + 1 + length goes to the end of the str length
            # REMEMBER THAT [:int] ALWAYS SKIPS INT
            i = j + 1 + length # start at first int after the str is iterated
        return result

