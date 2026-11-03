class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        keyword - "anagram" - hashmap

        inputs: s, t (strings)
        output: true/false (boolean)

        implementation:
        - track the frequency of each character
        - create 2 separate hash maps for each string s and t
        - at the end, compare the hash maps of s and t
        '''

        hashmap_s = {}
        hashmap_t = {}

        for s_char in s:
            if s_char not in hashmap_s:
                hashmap_s[s_char] = 1
            else: # if s_char in hashmap_s
                hashmap_s[s_char] += 1

        for t_char in t:
            if t_char not in hashmap_t:
                hashmap_t[t_char] = 1
            else: # if s_char in hashmap_t
                hashmap_t[t_char] += 1

        return hashmap_s == hashmap_t # same as returning true and else false