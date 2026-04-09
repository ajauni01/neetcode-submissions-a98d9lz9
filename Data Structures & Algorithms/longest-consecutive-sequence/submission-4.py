"""
Understand:
input = a list of nums
output = an integer
constraints = The length of the nums array need to be from 0 to 1000
and each element within the pow()
edge cases = empty array

Plan:
1. Convert the list to a set to remove duplicates and also get it back to the list
2. Check sequence and keep track of it
3. 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)>0:
            longest = 0
            unique_num = set(nums)

            for num in unique_num:
                length = 0
                if num-1 not in unique_num:
                    while num+length in unique_num:
                        length +=1
                    longest = max(longest, length)
            return longest 
        return 0              

                    


                   



        

        