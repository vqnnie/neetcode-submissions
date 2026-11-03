/*
input: nums
output: bool (true or false)
edge cases: 
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

pseudocode:
compare array to a set version of array
if not equal, return true

notes:
brute force is using 2 nested loops,
but we do not want that

we want to use a hash set
*/

#include <vector>
#include <set>
using namespace std; // allows me to use shit from the C++ library

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) { // returns bool
        set<int> setNums(nums.begin(), nums.end());
        if (nums.size() == setNums.size()) return false;
        return true;
    }
};