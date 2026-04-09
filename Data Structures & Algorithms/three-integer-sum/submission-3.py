"""
Understand:
input = a list of integers
output = an array of arrays with integers (indices)
constraints = 3 <= numss.length <= 100 and -pow(10,5) <= nums[i] <= pow(10,5)
edge cases = an empty array as an input

Plan =
1. The optimal approach is to sort the array first and we will
be able to use the two pointers method and avoid duplication.
2. Declare two variables, l and r with l=0, and r=len(nums)-1
3. The next step is to using a for loop with range, fix one of the num and finding the combination of other two nums with a minus that
becomes minus 1 with this. 
4. Use the for loop with enumerate to make sure to have both the index and value. 
5. Check if the value is greater than zero, if it is break out of the system.
6. Check duplicates
7. Fix one number and use repeated two pointer methods inside the while loop
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i]>0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, n-1

            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                if total_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1    
                elif total_sum < 0:
                    l +=1
                else:
                    r -=1        
        return res            


