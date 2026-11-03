class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        data structure: hashmap

        array of 0's from a-z : list of anagrams
        count : list of anagrams

        1. 00000000000000000000000000 for "act"
        2. 10100000000000000001000000 for "act"
        
        ----------------------------- : ["act", "cat"]
    
        '''

        anagram_hashmap = defaultdict(list) # allow lists as values

        for s in strs:
            # initiate count array for each str
            count = [0] * 26 # a-z is 26 letters
            
            for c in s:
                # ord() function returns an integer representing the Unicode code point of a single character
                count[ord(c) - ord('a')] += 1 # this finds the index of the letter in the array and replaces the 0 to 1
            count = tuple(count)
            anagram_hashmap[count].append(s)

        return list(anagram_hashmap.values()) # expects lists not dict_values