class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        open_bra = set(['[','{','('])
        if s[0] not in open_bra:
            return False
        stack = []
        for c in s:
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
