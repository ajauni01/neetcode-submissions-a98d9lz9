"""
Plan:
1. Declare a dict to store value and relevant index inside a for loop
2. 


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        res = []
        
        for i, num in enumerate(nums):
            complement_num = target - num
            if complement_num in store:
                res.append(store[complement_num])
                res.append(i)
            else:
                store[num] = store.get(num, i)
        return res            



        