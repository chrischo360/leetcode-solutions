# tc: O(n * n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # take a number and check if there is a sum for that target.
        nums = sorted(nums)
        res = []
        print(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: # skip it
                continue
            
            # find solution that adds up to nums
            target = nums[i] * -1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l + 1 < len(nums) and nums[l] == nums[l + 1]:
                        l += 1
                    while r >= 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
                elif nums[l] + nums[r] < target:
                    l += 1
                
                else:
                    r -= 1
            
        return res
            

