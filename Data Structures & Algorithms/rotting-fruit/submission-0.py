class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_fresh: int = 0
        q = deque()
        time: int = 0
        for u in range(len(grid)):
            for v in range(len(grid[0])):
                if grid[u][v]==2:
                    q.append((u,v,0))
                elif grid[u][v]==1:
                    total_fresh+=1
        if total_fresh==0:
            return 0
        delta = [(-1,0),(0,-1),(1,0),(0,1)]
        while q:
            u,v,time = q.popleft()
            for d_u,d_v in delta:
                r,c = u+d_u,v+d_v
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    total_fresh-=1
                    grid[r][c]=2
                    q.append((r,c,time+1))

        return time if total_fresh==0 else -1


        
        

