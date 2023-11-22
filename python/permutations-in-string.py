# tc: O(n) really ugly solution tbh

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = collections.defaultdict(int)
        s2map = collections.defaultdict(int)
        l, r = 0, len(s1) - 1

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1
        
        if s1map == s2map:
            return True
                
        while r < len(s2) - 1:
            if s1map == s2map:
                return True
            
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]
            l += 1
            r += 1
            s2map[s2[r]] += 1

            if s1map == s2map:
                return True

        return False

