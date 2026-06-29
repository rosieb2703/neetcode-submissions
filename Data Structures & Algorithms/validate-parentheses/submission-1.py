class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_mappings = {')' : '(', '}' : '{', ']' : '['}

        stack = []

        for c in s:
            if c in valid_mappings:
                print(c, stack)
                if stack and stack[-1] == valid_mappings[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if stack:
            return False
        else: 
            return True
                    

