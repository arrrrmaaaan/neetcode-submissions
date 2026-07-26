class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenBox = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                if (cell in seenRow[r] or cell in seenCol[c] or cell in seenBox[(r//3, c//3)]):
                    return False
                
                seenRow[r].add(cell)
                seenCol[c].add(cell)
                seenBox[(r//3, c//3)].add(cell)
        return True