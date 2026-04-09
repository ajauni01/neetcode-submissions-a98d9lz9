"""
Understand:
input = two strings
output = boolean (true or false)
constraints = s and t uppercase or any of s and t uppercase
edge cases = 

Plan:
1. Handle the constraints
2. declare the loop with a range
3. loop through the first string and see if the specific char also exists in the second string
4. store the second string elements in a dictionary
5. return True if the length of the first string matches with the length of the dict
6. Otherwise return false

"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s.islower() and t.islower():
            return Counter(s) == Counter(t)           
                
                    

                           

        

        