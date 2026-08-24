class DSU:
    def __init__(self,number_of_nodes):
        self.root = [i for i in range(number_of_nodes)]
        self.rank = [1]*number_of_nodes
    
    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX==rootY:
            return
        if self.rank[x]>self.rank[y]:
            self.root[rootY]=rootX
        elif self.rank[y]>self.rank[x]:
            self.root[rootX]=rootY
        else:
            self.root[rootX]=rootY
            self.rank[y]+=1
    
    def is_connected(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for edge in edges:
            dsu.union(edge[0],edge[1])

        return len({dsu.find(x) for x in range(n)})