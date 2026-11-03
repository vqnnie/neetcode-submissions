class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1: using hint 3, we know that the alphabet is a-z and 26 letters

        # when referring to the array, consider index and value

        hashmap = defaultdict(list) # returns [] by default if no key

        for string in strs:
            count = [0] * 26 # initialize array

            for char in string:
                count[ord(char) - ord('a')] += 1

                        # note: The ord() function in Python is a built-in function that returns 
                        # the Unicode code point of a given character. It takes a single character 
                        # (a string of length one) as an argument and returns an integer representing 
                        # its Unicode value.

                        # e.g. a --> 97, b --> 98, z --> 122
            
            hashmap[tuple(count)].append(string)

        return list(hashmap.values()) # expects a list, not dict_values
