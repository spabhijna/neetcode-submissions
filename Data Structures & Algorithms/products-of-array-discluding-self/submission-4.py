class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pred, post = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            pred[i] = pred[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(pred[i] * post[i])
        
        return res