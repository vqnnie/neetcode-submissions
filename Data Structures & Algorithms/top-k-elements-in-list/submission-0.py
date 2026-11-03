class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}  # num (key) : occurrences in list (value)

        # for loop that sets up the table for number of occurrences from 0 to n for each num

        freq = [[] for index in range(len(nums) + 1)] # add 1 because index stops at n - 1, but each num can occur n times, not n - 1
                                           # e.g. in [1, 1, 1, 1], 1 occurs 4 times, but index is from 0 to 3

        # this list comprehension matches:

        # freq = []
        # for i in range(len(nums) + 1):
        #     freq.append([])

        # example : nums = [1,2,2,3,3,3], k = 2
        # keys are 0 - 6, e.g. 0: ..., 1: ..., ... , 6: ...
        # freq = [[], [], [], [], [], [], []]
        # indices  0   1   2   3   4   5   6

        for num in nums:
            count[num] = 1 + count.get(num, 0) # .get retrieves value assigned to key in dict

        # now, we have a count dict that stores number of occurrences for each num
        # we want to append count.value() to an index in freq

        # count = {1: 1, 2: 2, 3: 3}

        for key, value in count.items():
            freq[value].append(key) # match value with index of freq, and append key

        topk = [] # output is a list

        for lst in range(len(freq) - 1, 0, -1): # start from the last index
            for num in freq[lst]:               # subtract -1 from len(freq) b/c freq has index 6, 1 greater than the index of the original list
                topk.append(num)

                if len(topk) == k: # when the result lst contains k items, return the result
                    return topk
