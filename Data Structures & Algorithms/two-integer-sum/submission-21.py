"""
Understand: 
input = array of integers, an integer
output = array of indices such that nums[i] and nums[j] == target
constraints = i != , 2 <= nums.length <= 1000, -10,000,000 <= nums[i] <= 10,000,000, -10,000,000 <= target <= 10,000,000
edge cases = empty set of array

Plan:
1. Handle all the constraints, and edge cases
2. Run a for loop (Outer for loop) with the range function. Withing the range function, we will have the length of nums array
3. The outer for loop will take one element from the nums array and will check with each element from the inner for loop and see if the combined elements is equal to the target
4. Take one element from the ineteger and compare it with every other element of the array
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if 2 <= len(nums) <= 1000 and -10000000 <= target <= 10000000:
            store_indices = []
            for i in range(len(nums)):
                if -10000000 <= nums[i] <= 10000000:
                    if i < len(nums) -1:
                        for j in range(i+1, len(nums)):
                            if nums[i] + nums[j] == target:
                                store_indices.append(i)
                                store_indices.append(j)
                                return store_indices

                    
        