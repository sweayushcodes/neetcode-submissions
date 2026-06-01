class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                value = board[i][j]

                if value == ".": 
                    continue

                if value in rows[i] or value in cols[j] or value in box[(i//3, j//3)]: 
                    return False
                
                rows[i].add(value)
                cols[j].add(value)
                box[(i//3,j//3)].add(value)
        
        return True

                

