"""
Understand:
input: an integer array
output: Boolean
constraints: empty array
edge case: empty case

Plan:
1. Declare a set variable
2. Run for loop within the array
2. Check whether each value already exists in the dictionary
3. if it already exists, return True, otherwise continue to add key and values in the dict
4. Finally return False
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False            

        

        