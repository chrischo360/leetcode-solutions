# tc: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: O(n)^2
        # optimized: O(n) - sliding window
        # uses a set to keep track of seen letters

        l = 0
        seenChars = set()
        res = 0

        for r in range(len(s)):
            if s[r] in seenChars:
                # increment left until it reaches the char
                while s[l] != s[r]:
                    seenChars.remove(s[l])
                    l += 1
                l += 1
            
            seenChars.add(s[r])
            res = max(res, r - l + 1)
        
        return res
