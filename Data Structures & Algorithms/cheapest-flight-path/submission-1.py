class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_dist = [float("inf")]*(n)
        adj_list = collections.defaultdict(list)
        edges = []
        for u,v,d in flights:
            adj_list[u].append((d,v))
            edges.append((u,v,d))

        min_dist[src] = 0

        for _ in range(k+1):
            m_d = min_dist.copy()
            updated = False
            for u,v,d in edges:
                if min_dist[v]>m_d[u]+d:
                    min_dist[v]=m_d[u]+d
                    updated = True
            if not updated:
                break
        
        return -1 if min_dist[dst]==float("inf") else min_dist[dst]



