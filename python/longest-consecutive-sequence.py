# tc: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        
        for num in numsSet:
            if num - 1 not in numsSet:
                # then we can start with this
                lces = 0
                startingNum = num
                while startingNum in numsSet:
                    lces += 1
                    startingNum = startingNum + 1
                
                res = max(res, lces)

        return res
