"""
Understand:
input = a string
output = boolean
constraints = 1 <= s.length <= 1000 and s is made up of only printable ASCII characters
edge cases = an empty string or the length of the string less than 1 or beyond 1000

Plan:
1. Declare L and R variables with L being 0 and R being len(string)-1
2. Loop inward for both of them
3. Create a minimum solution and iterate over it
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l,r = l+1, r-1
        return True         




        