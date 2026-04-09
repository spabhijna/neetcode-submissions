class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        # Define the boundaries of the virtual 1D array
        left, right = 0, (m * n) - 1
        
        return self.binary_search(left, right, matrix, target, n)

    def binary_search(self, l, r, matrix, target, n):
        while l <= r:
            mid = l + (r - l) // 2
            # Map mid index back to 2D coordinates
            row = mid // n
            col = mid % n
            
            mid_element = matrix[row][col]
            
            if mid_element == target:
                return True
            elif mid_element < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False