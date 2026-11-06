class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        CONVERTING 3 SUM INTO 2 SUM - TWO POINTER METHOD

        time complexity: O(n^2)
        space complexity: O(1) or O(n)

        -3, -2, -2, 0, 1, 2, 3, 3
        i    l                  r

        things to keep in mind:
        - we don't want there to be a repeated value at i 
        - same for l and r, no repeated value at l and no repeated value at r

        '''

        nums.sort()
        res = []

        for i, n in enumerate(nums): # iterate through each n in nums and track its i
            # check if we already saw the value at i
            # i must be greater than 0, i.e. i cannot be the first value because there is no value before that
            if i > 0 and n == nums[i - 1]:
                continue

            # now we just find which l and r values add with n to equal 0
            l = i + 1 # l is the pointer after i
            r = len(nums) - 1

            while l < r:
                curr_sum = n + nums[l] + nums[r]
                
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res

