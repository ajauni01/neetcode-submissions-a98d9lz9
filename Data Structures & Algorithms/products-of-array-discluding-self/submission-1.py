"""
Understand:
input = a list of integers
output =  a list of integers
constraints = 2 <= nums.length <= 100 and -20 <= nums[i] <= 20
edge cases = empty list 

Plan:
1. We will use prefix and suffix sum
2. Think of a array split into everything to the left of i
and everyhting to the right of i
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *=postfix
            postfix *=nums[i]

        return res      


            



