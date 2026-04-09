"""
Plan:
1. Loop through the array
2. num[i]-target

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in res:
                return [res.get(complement),i]
            res[n] = i   

              
