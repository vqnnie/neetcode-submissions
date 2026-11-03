/*
inputs: s, t
outputs: true, false
edge cases:
- s is empty
- t is empty
- both s and t are empty

pseudocode:
if s and t are "" return true
if s or t are "" return false
return sorted s and sorted t

notes:
there are 2 ways to go about this, 1 way is to create 
a hashmap, and another way is to sort both strings and 
compare them to see if they are equal

*/

#include <algorithm> // allows me to use sort() function

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s == "" && t == "") return true;
        if (s == "" || t == "") return false;
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s == t;
    }
};
