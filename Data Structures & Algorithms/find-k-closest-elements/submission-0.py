class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minL = float('inf')
        minI = -1
        for i, num in enumerate(arr):
            if abs(x - num) < minL:
                minL = abs(x - num)
                minI = i
        
        left = minI
        right = minI + 1
        result = []

        while len(result) < k:
            if left >= 0 and right < len(arr):
                distL = abs(arr[left] - x)
                distR = abs(arr[right] - x)

                if distR >= distL:
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
                
            elif left >= 0:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        
        return sorted(result)

            
            

            
            



        