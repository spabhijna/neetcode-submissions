class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = 0, 0, 0  # Added the third 0
        temp = nums1[:m]   # Only copy the elements that matter
        
        while i < m and j < n:
            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        # Catch remaining elements in temp
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1
            
        # Catch remaining elements in nums2
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1