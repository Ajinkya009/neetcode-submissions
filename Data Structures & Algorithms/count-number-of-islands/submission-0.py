class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        delta = [(-1,0),(0,-1),(0,1),(1,0)]
        num_of_islands = 0
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]=="0":
                return
            grid[r][c]="0"
            for d_r,d_c in delta:
                dfs(r+d_r,c+d_c)
            return
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    dfs(r,c)
                    num_of_islands+=1
        return num_of_islands