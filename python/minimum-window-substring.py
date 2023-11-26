# tc: O(n * 26)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def validSubstring(s, t):
            for c in t:
                if c not in s:
                    return False
                if s[c] < t[c]:
                    return False
            return True

        res = ""
        resLength = float("inf")
        l = 0
        sCount = collections.defaultdict(int)
        tCount = Counter(t)

        for r in range(len(s)):
            sCount[s[r]] += 1

            while validSubstring(sCount, tCount):
                if (r - l + 1) < resLength:
                    res = s[l:r+1]
                    resLength = len(res)
                
                sCount[s[l]] -= 1
                if sCount[s[l]] == 0:
                    del sCount[s[l]]
                l += 1

        return res
