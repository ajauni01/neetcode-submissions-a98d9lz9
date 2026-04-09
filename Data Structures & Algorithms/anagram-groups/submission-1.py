"""
Understand:
input = Array of strings
output = array with anagrams and all the anagrams should be in a ist separately
constraints = 1 <= strs.length, 0 <= strs[i].length <=100
edge cases = empty list of array, return empty array with the empty string

Plan:
1. Declare an array that will hold the list
2. loop through the list of array
3. for each string, at first we will look for the same length then we will check if the same length string also contains the same characters
4. If found match, we will store both of them in the store_anagrams
5. if the string is equal to the length of another strings then

pseudocode:
 for str in strs:
    store it in the tmp store
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)   
        return list(res.values())     
              
            
            