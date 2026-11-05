class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        TWO POINTER METHOD

        things to keep in mind:
        - we want to return 1-indexed indices, meaning the first value begins at index 1 not 0
        - the array is SORTED in non-decreasing/ascending order.. this means that shifting the l pointer the right results in a larger value, while shifting the r pointer to the left results in a smaller value
        - we want to return the indices to two numbers which means there isn't going to be one indice of one number that equals target

        implementation:
        - we want to add the numbers at the l and r pointers and compare them to the target
        - if the sum is greater than target, move r pointer to the left (r -= 1) to decrease the sum
        - if the sum is less than target, move l pointer ot the right (l += 1) to increase the sum
        '''

        l = 0 # cannot start at 1 because python uses 0 indexed arrays
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r] # add the values at the l pointer and the r pointer

            if curr_sum > target:
                r -= 1
                continue

            if curr_sum < target:
                l += 1
                continue

            if curr_sum == target:
                return [l + 1, r + 1]
