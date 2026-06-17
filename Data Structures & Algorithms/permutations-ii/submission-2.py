class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        solutions = set()  # Use a set to handle duplicates
        visited = [False] * len(nums)
        
        def backtrack(state):
            if len(state) == len(nums):
                # Lists aren't hashable, so convert to a tuple for the set
                solutions.add(tuple(state)) 
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # No duplicate check here anymore!
                
                visited[i] = True
                state.append(nums[i])
                backtrack(state)
                state.pop()
                visited[i] = False
                
        backtrack([])
        # Convert tuples back to lists for the expected return type
        return [list(s) for s in solutions]