"""
Plan:
1. Get the frequency of each value in a dictionary
2. Get the key and values using dict.items()
3. using the

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        res = []

        for num in nums:
            freq_count[num] = freq_count.get(num, 0)+1

        store = [[] for _ in range(len(nums)+1)]
        for key, value in freq_count.items():
            store[value].append(key)

        for i in range(len(store)-1,-1,-1):
            for n in  store[i]:
                res.append(n)
            if len(res) == k:
                return res    
            