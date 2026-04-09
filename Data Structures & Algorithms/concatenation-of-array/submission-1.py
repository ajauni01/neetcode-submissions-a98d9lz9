"""
Understand:
input - array
output - concatenation of two nums array
constraint -> 0 <= i < n, 1 <= nums.length <= 1000 & 1 <= nums[i] <= 1000
edge case - empty num array input

Plan:
1. Run a while loop and continue to copy value from the given array and insert it to the ans array
2.until the length of answer array is not the double of the given array
3. copy the value of nums[i] to the ans[i]
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans    




        