"""
Understand:
input = A list of strings
output = a list of list of string anagrams
constraints = 1 <= strs.length <= 1000 and 0 <= strs[i].length <= 100
and strs[i] is made of lowercase English letters
edge cases = empty list of strings

Plan: 
1. create a variable with dict
2. Loop through the list 
3. We need to use the bucket sort algorithm and declare 
the anagram_count signature
4. 

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for each_str in strs:
            anagram_count = [0]*26

            for s in each_str:
                value = ord(s)-97
                anagram_count[value] +=1
            anagram_dict.setdefault(tuple(anagram_count),[]).append(each_str)

        return list(anagram_dict.values())      

        