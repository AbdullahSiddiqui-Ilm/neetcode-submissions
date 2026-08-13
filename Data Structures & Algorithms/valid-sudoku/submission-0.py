class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        for i in range(len(board)):
            row = [x for x in board[i] if x != "."]
            column = [row[i] for row in board if row[i] != "."]
            hashset_row, hashset_column = set(row), set(column)
            if len(hashset_row) != len(row) or len(hashset_column) != len(column):
                return False
            for c in range(9):
                if board[i][c] in squares[(i // 3, c // 3)]:
                    return False
                if board[i][c] != ".":
                    squares[i // 3, c // 3].add(board[i][c])
        return True
        
            

        