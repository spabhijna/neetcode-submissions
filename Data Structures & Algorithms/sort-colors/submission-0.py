class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Step 1: Count occurrences
        counts = {0: 0, 1: 0, 2: 0}
        for num in nums:
            counts[num] += 1
        
        # Step 2: Overwrite nums in-place
        index = 0
        for color in [0, 1, 2]:
            for _ in range(counts[color]):
                nums[index] = color
                index += 1