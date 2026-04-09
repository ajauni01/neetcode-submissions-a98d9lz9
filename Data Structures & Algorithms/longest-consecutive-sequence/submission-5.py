"""
Understand:
input: an array of integers
output: integer
constraints = 0 <= nums.length <= 100
and -pow(10,9) <= nums[i] <= pow(10,9)
edge caes: an empty list

Plan:
1. Directly convert the array to a hash set (This is the magic trick) 
1. Loop through the array
2. Figure out the beginning of a num by checking if the previous number exists
3. Figure out if the +1 of the beginning exist in the nums if so continue the loop and inccrease the length
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        sequence = 0

        for num in numset:
            if num-1 not in numset:
                length = 0
                while num+length in numset:
                    length +=1
                sequence = max(length, sequence)
        return sequence            
        