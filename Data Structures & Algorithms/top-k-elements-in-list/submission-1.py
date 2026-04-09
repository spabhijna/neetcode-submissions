class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        arr = []
        for key, value in d.items():
            arr.append([value, key])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        
        