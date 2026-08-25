class DSU:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self,x):
        if self.root[x]==x:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX==rootY:
            return False
        if self.rank[rootX]>self.rank[rootY]:
            self.root[rootY]=rootX
        elif self.rank[rootY]>self.rank[rootX]:
            self.root[rootX]=rootY
        else:
            self.root[rootX]=rootY
            self.rank[rootY]+=1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        dsu = DSU(n)

        for i in range(n):
            x,y = points[i][0],points[i][1]
            for j in range(i+1,n):
                p,q = points[j][0],points[j][1]
                distance = abs(p-x)+abs(q-y) 
                edges.append((distance,i,j))
        
        #edges.sort()
        heapq.heapify(edges)
        output = 0
        edges_used = 0
        while edges:
            dist,x,y = heapq.heappop(edges)
            if dsu.union(x,y):
                output+=dist
                edges_used+=1
            if edges_used==n-1:
                break

        return output
            