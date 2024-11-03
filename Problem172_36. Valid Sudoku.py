class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] !=".":
                    s.add(board[i][j])

        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i] !=".":
                    s.add(board[j][i])

        start=[(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]
        for i,j in start:
            s=set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if board[r][c] in s:
                        return False
                    elif board[r][c] !=".":
                        s.add(board[r][c])
        return True
