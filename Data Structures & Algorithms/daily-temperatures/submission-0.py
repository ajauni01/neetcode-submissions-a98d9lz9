"""
Understand:
input = an array of integers
output = an array of integers
constraints = (1 <= temperatures.length <= 100) and (1 <= temperatures[i] <= 100)
edge cases = empty array of integers

Plan:
1. Loop through the given array with enumeration
2. Store both index and value
3. if the temperature is greater, then run the while loop
4. Pop the last tuple (index and value)
5. get the index and value from the poped stack
6. Update the result array with the days

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                days = i - stackIndex
                result[stackIndex] = days
            stack.append((i, temp))    
        return result            



        