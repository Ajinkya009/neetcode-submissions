class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_dist = [float("inf")]*(n)
        adj_list = collections.defaultdict(list)

        for u,v,d in flights:
            adj_list[u].append((d,v))

        min_dist[src] = 0
        pq = [(0,0,src)]
        heapq.heapify(pq)
        visited = {}
        while pq:
            dist,visited_nodes,node = heapq.heappop(pq)
            if node==dst: return dist
            if visited_nodes>k or ((node,visited_nodes) in visited and visited[(node,visited_nodes)]<dist):
                continue
            visited[(node,visited_nodes)] = dist
            for nei_d,nei in adj_list[node]:
                print(nei_d,nei)
                d = nei_d+dist
                heapq.heappush(pq,(d,visited_nodes+1,nei))
        return -1



