"""
Plan:
1. we need to use two pointer algorithm to solve this problem
2. 

"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m 
        return nums[l]                


                           
            

        