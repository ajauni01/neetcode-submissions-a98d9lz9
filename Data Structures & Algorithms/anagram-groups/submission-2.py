"""
Plan:
1. 


"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        
        for s in strs:
            anagram_count = [0] * 26 
            for c in s:
                anagram_count[ord(c)-ord("a")] +=1
            anagrams_dict[tuple(anagram_count)].append(s)

        return list(anagrams_dict.values() )

                


