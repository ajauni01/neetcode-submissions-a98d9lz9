"""
Understand: 
input = array of integers, an integer
output = array of indices such that nums[i] and nums[j] == target
constraints = i != , 2 <= nums.length <= 1000, -10,000,000 <= nums[i] <= 10,000,000, -10,000,000 <= target <= 10,000,000
edge cases = empty set of array

Plan:
1. Declare a dictionary
2. Loop through the list using enumeration and get the index

pseudocode:
store_dict = {}

for index, item in enumerate(nums):
    store_dict[index] = item
    remaining_value = target - nums[index]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_index = []
        store_dict = {}

        for i in range(len(nums)):
            remaining_value = target - nums[i]
            if remaining_value in store_dict:
                store_index.append(store_dict[remaining_value])
                store_index.append(i)
                return store_index
            store_dict[nums[i]] = i
        return store_index 

        

                    
        