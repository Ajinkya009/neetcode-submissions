class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        delta = [(-1,0),(0,-1),(0,1),(1,0)]
        num_of_islands = 0
        max_area = 0
        area = 0
        def dfs(r,c):
            temp_area = 0
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                return 0
            grid[r][c]=0
            for d_r,d_c in delta:
                temp_area+=dfs(r+d_r,c+d_c)
            return temp_area+1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area = max(area,max_area)
        return max_area