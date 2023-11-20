# tc: O(9 * 9)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep three dictionaries. each dictionary contains a set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        matrix = collections.defaultdict(set)

        R, C = len(board), len(board[0])

        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in matrix[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                matrix[(r // 3, c // 3)].add(board[r][c])
        
        return True
