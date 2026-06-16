class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        combination = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                combinations.append(''.join(combination))
                return
            if openN < n:
                combination.append('(')
                backtrack(openN+1, closedN)
                combination.pop()
            if closedN < openN:
                combination.append(')')
                backtrack(openN, closedN+1)
                combination.pop()
        backtrack(0,0)
        return combinations
        
        