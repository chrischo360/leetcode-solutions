# tc: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generateParen(open, closed, str):
            if len(str) == n * 2:
                res.append(str)
                return
            
            if open < n:
                generateParen(open + 1, closed, str + "(")

            if open > closed:
                generateParen(open, closed + 1, str + ")")

        generateParen(0, 0, "")
        return res
