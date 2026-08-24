class DSU:
    def __init__(self):
        self.root = [i for i in range(1001)]
        self.rank = [0]*1001

    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX==rootY:
            return True
        if self.rank[rootX]>self.rank[rootY]:
            self.root[rootX]=rootY
        elif self.rank[rootX]<self.rank[rootY]:
            self.root[rootY]=rootX
        else:
            self.root[rootX]=rootY
            self.rank[rootX]+=1
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for u,v in edges:
            if dsu.union(u,v):
                return [u,v]
        return []