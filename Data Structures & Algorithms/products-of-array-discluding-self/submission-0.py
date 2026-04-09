"""
U
input= an array of integers
output = array of integers
constraints = 2 <= nums.length <= 1000 and -20 <= nums[i] <= 20 and if the product is more than 32 bit
edge cases = empty array

Plan:
1. Declare the result array with the default value 1 length 5
2. Work on the prefix array
3. 

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *=nums[i]
        return res    

