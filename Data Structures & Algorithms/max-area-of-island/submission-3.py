class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        delta = [(-1,0),(0,-1),(0,1),(1,0)]
        num_of_islands = 0
        max_area = 0
        area = 0
        def dfs(r,c):
            nonlocal area
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                return
            grid[r][c]=0
            area+=1
            for d_r,d_c in delta:
                dfs(r+d_r,c+d_c)
            return
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    area = 0
                    dfs(r,c)
                    print(area)
                    max_area = max(area,max_area)
        return max_area