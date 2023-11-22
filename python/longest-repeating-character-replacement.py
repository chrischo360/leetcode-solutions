# tc: O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        charCount = collections.defaultdict(int)
        mostSeenChar = ""
        charCount[mostSeenChar] = 0

        for r in range(len(s)):
            # add the s[r]
            charCount[s[r]] += 1
            if charCount[s[r]] > charCount[mostSeenChar]:
                mostSeenChar = s[r]
            
            # check if it is valid and if not, move left
            while charCount[mostSeenChar] + k < (r - l + 1):
                charCount[s[l]] -= 1
                for char in charCount:
                    if charCount[char] > charCount[mostSeenChar]:
                        mostSeenChar = char
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res


