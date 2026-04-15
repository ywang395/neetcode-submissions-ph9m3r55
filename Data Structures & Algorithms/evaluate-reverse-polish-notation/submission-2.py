class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+': 0,'-' : 0, '/': 4 ,'*': 4 }
        for token in tokens : 
            if token in operator: 
                left = int(stack.pop())     
                right = int(stack .pop())
                
                if token == '+':
                    stack.append (right + left)
                
                elif token ==  '-':
                    stack.append (right - left)
                    
                elif token ==  '*':
                    stack.append (right * left)
                    
                elif token ==  '/':
                    stack.append (right / float(left))
                        
            else: 
                stack.append(token)
        return int(stack.pop())