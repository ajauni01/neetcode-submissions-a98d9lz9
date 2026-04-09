"""
Understand:
input = an array of strings
output = an integer
constraints = 1<=tokens.length <= 1000 and tokens[i] is either '+', '-', '*' or '/' or 
a string representing an integer in the range [-100,100]
edge cases = an empty array of string

Plan:
1. 
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))  
            else:
                stack.append(int(token))
        return stack[0]                 

            

        
                       




        