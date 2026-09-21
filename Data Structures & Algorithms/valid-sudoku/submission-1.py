class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        for i in range(len(board)):
            row = [x for x in board[i] if x != "."]
            columns = [row[i] for row in board if row[i] != "."]
            hashset_rows, hashset_columns = set(row), set(columns)

            if len(hashset_rows) != len(row) or len(hashset_columns) != len(columns):
                return False
            
            
            for c in range(len(board)):
                if board[i][c] in squares[i // 3, c // 3]:
                    return False
                elif board[i][c] != ".":
                    squares[i // 3, c // 3].add(board[i][c])
                    
        return True

"""
pattern:

- Take integers of all rows and columns and store in arrays. we want to check if any
duplicates exist, so lists are converted to sets to compare lengths. if different, return False
as we know a duplicate must exist in either rows or columns.

- If lengths are same, we iterate through each row and check two things:
    1. If the current value on the board already exists in squares(a dictionary with a key of x, y acting as co-ordinates
    to split the sodoku board into 9. eg: 0, 0 - 0, 1 - 0, 2 - these represent the three top boxes on the board)
    then we know there is a duplicate in the current square of sodoku board.
    2. If that condition is False, we know the that its not a duplicate, so we check if its an actual integer, as blank
    values are represented as ".".

- Return True if we exit outer loop completely.
"""
            

        