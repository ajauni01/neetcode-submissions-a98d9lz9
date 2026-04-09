class Solution:
    def isValid(self, s: str) -> bool:
        dict_store = {'(':')', '{':'}','[':']'}
        opening = ['(','{','[']
        opening_stack = []

        for char in s:
            if char in opening:
                opening_stack.append(char)
            else:
                if not opening_stack or dict_store.get(opening_stack.pop(),0) != char:
                    return False
        return not opening_stack            