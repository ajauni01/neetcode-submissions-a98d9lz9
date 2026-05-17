"""
Understand:
input = Two arrays (position and speed)
output = An integer
constraints =  n == position.length == speed.length
1 <= n <= 1000 and 0 <target <= 1000 and 0 < speed[i] <= 100
and 0 <= position[i] < target
edge cases = an empty set of arrays or nagative values in the array

Plan:
1. Zipped two arrays into one array with position and speed
2. Sort the zipped arrays in reverse order to starting with the position closer to the target
3. From there, based on the speed, calculate the time it takes to reach the target
4. 


"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = zip(position, speed)
        descending_pairs = sorted(pairs, reverse=True)

        for each_pair in descending_pairs:
            time = (target - each_pair[0])/each_pair[1]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        return len(stack)            



        