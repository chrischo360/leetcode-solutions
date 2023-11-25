# tc: O(n * m)

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, freeItems):
            if (i, freeItems) in dp:
                return dp[(i, freeItems)]
            
            if i >= len(prices):
                return 0
        
            dp[(i, freeItems)] = 0
            
            if freeItems > 0: # we have the choice of taking it for free or not
                dp[(i, freeItems)] = min(dfs(i + 1, freeItems - 1), prices[i] + dfs(i + 1, i + 1))
            else:
                dp[(i, freeItems)] = prices[i] + dfs(i + 1, i + 1)
                
            return dp[(i, freeItems)]
        
        return dfs(0, 0)
