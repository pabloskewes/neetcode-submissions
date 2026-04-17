class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(n):
            for j in range(n):
                x = board[i][j]
                if x == ".":
                    continue
                square = squares[i // 3][j // 3]
                if x in rows[i] or x in cols[j] or x in square:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                square.add(x)
        
        return True