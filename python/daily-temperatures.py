# tc: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                day = stack.pop()
                res[day] = i - day
            
            stack.append(i)
        
        return res
