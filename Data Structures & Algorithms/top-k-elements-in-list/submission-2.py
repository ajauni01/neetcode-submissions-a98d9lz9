"""
Understand:
input= list
output= list
constraints = 1 <= nums.length <= pow(10,4), -1000 <= nums[i] <= 1000 
1 <= k <= number of distinct elements in sums
edge cases = empty list

Plan:
1. Loop through the nums
2. use dict to keep track of the frequencies
3. we will use bucket sort to group numbers based on the frequencies
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        for num in nums:
            count_bucket = [[] for i in range(len(nums)+1)]
            count = {}
            
            for num in nums:
                count[num] = count.get(num, 0)+1

            for n,c in count.items():
                count_bucket[c].append(n)

                res = []
            for i in range(len(count_bucket)-1,-1,-1):
                for n in count_bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res  
                
                
                




