"""
Understand:
i = an array of integers, a target
o = an array of indices such that nums[i] + nums[j] == target and i != j
c = 2 <= nums.length <= 1000, -10,000,000 <= nums[i] <= 10,000,000, -10,000,000 <= target <= 10,000,000
e = empty array, negative target

Plan:
1. Declare an empty list
2. Take care of the constraints and edge cases
3. Find all the possible combination of i and j that will match the target with the nested for loop
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_index = []
        if nums and -10000000 <= target <= 10000000 and 2 <= len(nums) <= 1000:
            for i in range(len(nums)):
                if i < (len(nums) - 1):
                    for j in range(i + 1, len(nums)):
                        if nums[i] + nums[j] == target:
                            store_index.append(i)
                            store_index.append(j)
                            return store_index
                    
        





        