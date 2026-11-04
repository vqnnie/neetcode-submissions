class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        inputs: int array nums, int k
        output: int k

        notes:
        - use a hashmap to track num : freq for each num in nums
        - use an array to track freq (index) and list of num (value) that has the same freq
        - use an array to store top k elements
        - read top k from last value in freq array because the highest index means the highest freq/occurences
        - return top k if len(topk) == k
        '''

        freq_hashmap = {}
        freq_array = []

        # initialize list for each index starting from 0 to len(nums), so you have to add +1 to len(nums)
        for i in range(len(nums) + 1):
            freq_array.append([])

        # track num : freq for each num in nums
        for n in nums:
            if n in freq_hashmap:
                freq_hashmap[n] += 1
            else:
                freq_hashmap[n] = 1

        for n, freq in freq_hashmap.items():
            freq_array[freq].append(n) # map each freq to the index of freq_array and n to the value of freq_array

        top_k = []

        for i in range(len(freq_array) - 1, -1, -1): # includes len(nums) - 1 and excludes -1
            for n in freq_array[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k