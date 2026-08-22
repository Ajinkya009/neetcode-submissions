class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_of_rows, num_of_cols = len(board), len(board[0])
        delta = [(-1,0),(0,-1),(1,0),(0,1)]
        def dfs(r,c):
            if r<0 or r>=num_of_rows or c<0 or c>=num_of_cols or board[r][c]!="O":
                return
            board[r][c]="T"
            print(r,c)
            for d_r,d_c in delta:
                dfs(r+d_r,c+d_c)
        
        for r in range(num_of_rows):
            for c in range(num_of_cols):
                if r==0 or r==num_of_rows-1 or c==0 or c==num_of_cols-1:
                    dfs(r,c)
        
        for r in range(num_of_rows):
            for c in range(num_of_cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
        
        return
        