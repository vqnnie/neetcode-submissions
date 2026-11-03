/* brute force solution

pseudocode:

for i from 0 to nums size
    for j from i to nums size
        if nums[i] + nums[j] == target and i!=j
            if i > j
                return [i,j]
            return [j,i]

*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target && i!=j) {
                    if (i < j) { // return smaller index first
                        return {i,j}; // c++ uses { } for lists
                    } return {j,i};
                }
            }
        }
    }
};
