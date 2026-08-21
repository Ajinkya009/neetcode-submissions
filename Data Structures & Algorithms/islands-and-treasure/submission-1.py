class Solution:
    def islandsAndTreasure(self, mat: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for u in range(len(mat)):
            for v in range(len(mat[0])):
                if mat[u][v]==0:
                    q.append((u,v,0))
                    visited.add((u,v))
        delta = [(-1,0),(0,-1),(1,0),(0,1)]
        while q:
            r,c,dist = q.popleft()
            for d_r,d_c in delta:
                u,v = r+d_r,c+d_c
                if 0<=u<len(mat) and 0<=v<len(mat[0]) and (u,v) not in visited and mat[u][v]!=-1:
                    mat[u][v] = dist+1
                    visited.add((u,v))
                    q.append((u,v,dist+1))
        return