# tc: O(n)

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        res = 0
    
        hBarSet = set(hBars)
        vBarSet = set(vBars)
        
        hBarLCS = 0
        for hBar in hBars:
            currHBarLCS = 0
            currNum = hBar
            
            if hBar - 1 not in hBarSet: # doesn't have a previous number
                
                while currNum in hBarSet:
                    currHBarLCS += 1
                    currNum += 1
                    
            hBarLCS = max(hBarLCS, currHBarLCS)
        
        vBarLCS = 0
        for vBar in vBars:
            currVBarLCS = 0
            currNum = vBar
            
            if vBar - 1 not in vBarSet: # doesn't have a previous number
                
                while currNum in vBarSet:
                    currVBarLCS += 1
                    currNum += 1
                    
            vBarLCS = max(vBarLCS, currVBarLCS)
        return (min(hBarLCS, vBarLCS) + 1) ** 2
