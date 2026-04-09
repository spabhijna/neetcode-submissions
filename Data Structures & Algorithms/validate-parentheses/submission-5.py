class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_bra = set(['[','{','('])
        stack = []
        for c in s:
            if c not in open_bra and not stack:
                return False
            if c in open_bra:
                stack.append(c)
            elif stack:
                b = stack.pop()
                if c == ']' and b != '[':
                    return False
                if c == '}' and b != '{':
                    return False
                if c == ')' and b != '(':
                    return False
        
        if stack:
            return False
        return True
