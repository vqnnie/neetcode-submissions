class Solution:
    '''
    encode:
    input: strs (list)
    output: encoded_str (string)

    decode:
    input: encoded_str
    output: strs

    we want to track the number of char are in one string and use a delimiter
    this delimiter tells us that this is the start of a string
    before the delimiter is a number representing the number of char in the string

    len(s) - number of char
    '''

    def encode(self, strs: List[str]) -> str:
        encoded_str = "" # initialize an empty string

        for s in strs:
            # example: the s is "cat" so this adds 3#cat to encoded_str
            encoded_str += str(len(s)) + "#" + s # len(s) outputs an int, but we want it to be a str 

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0 # initialize an empty list and an index that keeps track of each c

        while i < len(s): # i goes through each c of encoded_str
            j = i # j is a second pointer that is the c after i. the c on the right of i's c
            # j is used to land on the delimiter "#"

            while s[j] != "#": # we are still at an int, we didn't reach the delimiter "#" yet
                j += 1 # second pointer continues to move to next c, while i remains in place

            # by now j = "#"
            s_length = int(s[i:j]) # i:j are numbers but still a string. we must convert into int.
            decoded_strs.append(s[j + 1 : j + 1 + s_length]) # j + s_length reaches the last char of the string, but range excludes last char so we must + 1.
            i = j + s_length + 1 # + 1 is the next c after the whole string

        return decoded_strs


            