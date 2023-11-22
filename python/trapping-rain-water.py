# tc: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        maxLeft = []
        maxRight = []

        left = 0
        for i in range(len(height)):
            maxLeft.append(left)
            left = max(left, height[i])
        
        right = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight = [right] + maxRight
            right = max(right, height[i])
        
        for i in range(len(height)):
            if height[i] < min(maxLeft[i], maxRight[i]):
                res += (min(maxLeft[i], maxRight[i]) - height[i])

        return res
