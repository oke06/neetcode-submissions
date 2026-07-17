class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            # if c is a closing parenthesis
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: #put c on top of stack if open parenthesis
                stack.append(c)
        
        return len(stack) == 0
        