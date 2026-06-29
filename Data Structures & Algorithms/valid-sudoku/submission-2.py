class Solution:

    def check_row_and_cols(self, board: List[List[str]]) -> bool:

        # Check row
        for row in board:
            seen_row = defaultdict()
            for num in row:
                if num == ".":
                    continue
                elif num in seen_row:
                    return False
                else:
                    seen_row[num] = "T"

        # Check col
        i=0
        while i < len(board[0]):
            col = []
            for row in board:
                col.append(row[i])

            seen_col = defaultdict()
            for num in col:
                if num == ".":
                    continue
                elif num in seen_col:
                    return False
                else:
                    seen_col[num] = "T"
            i+=1
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check full board
        valid = self.check_row_and_cols(board)

        if not valid:
            return False

        # Create square
        j = 0
        while j < len(board[0]):
            i = 0
            while i < len(board[0]):
                mini_board = []
                for row in board[j:j+3]:
                    sub_row = row[i:i+3]
                    for num in sub_row:
                        mini_board.append(num)
                
                valid = self.check_row_and_cols(mini_board)
                if not valid:
                    return False
                else:
                    i += 3
            j += 3
        
        return True
