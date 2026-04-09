"""
Understand =
input: a list of string
output: a list of string
constraints: The length of the list of string needs 
to be from 0 to 100 exlusive (0<=strs.length < 100),
 and the length of each element needs to be from zero to 200 exlusive 
 (0<= strs[i].length < 200). Also, the strs[i] contains only the UTF-8 characters
 edge cases: empty list of string or anything outside of the constraints

 Plan =
1. Loop through the list of string
2. 


"""

class Solution:
     
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string    


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while(i < len(s)):
            j=i
            while(s[j] != "#"):
                j+=1
                length = int(s[i:j])
            i = j+1+length
            res.append(s[j+1:j+1+length])
        return res            




