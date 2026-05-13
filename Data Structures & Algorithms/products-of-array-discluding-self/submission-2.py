"""
Plan:
1. Loop through the given array
2. Declare a result array
3. 

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix_value = 1
        postfix_value = 1

        for i in range(len(nums)):
            res[i] = prefix_value
            prefix_value *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix_value
            postfix_value *= nums[i]
        return res        
        