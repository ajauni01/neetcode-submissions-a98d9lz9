"""
Understand:
Input = a list of non-negative integers
Output = an integer
Constraints = 1 <= height.length <= 1000 and 0 <= height[i] <= 1000
Edge cases = an empty list of array

Plan: 
1. Declare a total_trapped_water variable to keep track of the total trapped water
2. Track max_left and max_right


"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        trapped_water = 0

        while l<r:
            if left_max <= right_max:
                water = left_max - height[l]
                if water>0:
                    trapped_water += water
                l+=1
                left_max = max(left_max, height[l])    
    

            else:
                water = right_max - height[r]
                if water>0:
                    trapped_water += water
                r-=1
                right_max = max(right_max, height[r] ) 
                
        return trapped_water              


                 

        