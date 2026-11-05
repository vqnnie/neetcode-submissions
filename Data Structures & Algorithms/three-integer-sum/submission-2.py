class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        TWO POINTER SQUEEZE TECHNIQUE

        inputs: nums (int array)
        outputs: list of lists

        things to keep in mind:
        - i, j, and k are all distinct and the output should not contain duplicate triplets
        - we don't want to have the same numbers from a triplet as another triplet
        - we are going to use 3 pointers: i, low, high

        importan notes:
        - sort nums in numerical order first so we know that we can move low pointer to the right to increase the sum and high pointer to the left to decrease the sum

        -3, -2, -2, 0, 1, 2, 3, 3
        i  low                 high

        check if sum == 0
    
        '''

        nums.sort() # IMPORTANT!
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # value at i is NOT the value at the first index 0
                continue # move to the next i in the for loop
            # we want to redefine low and high for each i
            low = i + 1
            high = len(nums) - 1

            while low < high: # now we are gonna move low and high pointers through the rest of the array
                curr_sum = nums[i] + nums[low] + nums[high]

                if curr_sum > 0:
                    high -= 1
                elif curr_sum < 0:
                    low += 1
                elif curr_sum == 0:
                    res.append([nums[i], nums[low], nums[high]]) # we found a solution, but we must keep looking for more low and high values that add with the value at i to get 0 
                    low += 1
                    high -= 1
                    # skip low and high values we've already seen
                    while low < high and nums[low] == nums[low - 1]: # checks number on left side of low
                        low += 1
                        continue
                    while low < high and nums[high] == nums[high + 1]: # checks number on the right side of high
                        high -= 1
                        continue
                
        return res