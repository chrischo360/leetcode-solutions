class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output index = nums on left * nums on right
        # keep an additional array that tracks the product of all the nums on the right

        left = []
        right = []

        left.append(1)

        for num in nums:
            left.append(left[-1] * num)
        
        left.pop()

        right.append(1)
        for i in range(len(nums) - 1, -1, -1):
            right.append(right[-1] * nums[i])
        
        right.pop()
        right = right[::-1]
        res = []

        for i in range(len(left)):
            res.append(left[i] * right[i])

        return res
