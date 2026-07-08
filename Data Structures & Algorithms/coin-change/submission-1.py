class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recursion(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if amt in memo:
                return memo[amt]
            
            min_coins = float('inf')
            for i in range(len(coins)):
                res = recursion(amt-coins[i])
                if res != float('inf'):
                    min_coins = min(1 + res, min_coins)
            memo[amt] = min_coins
            return min_coins
        ans = recursion(amount)

        return ans if ans != float('inf') else -1



        