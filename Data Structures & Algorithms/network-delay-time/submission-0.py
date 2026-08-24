class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_times = [float('inf')]*(n+1)
        min_times[k] = 0
        min_times[0] = 0
        seen = set()
        adj_list = collections.defaultdict(list)

        for u,v,t in times:
            adj_list[u].append((t,v))
        q = [(0,k)]
        heapq.heapify(q)
        print(q)
        while q:
            t,node = heapq.heappop(q)
            if node in seen:
                continue
            seen.add(node)
            for time,nei in adj_list[node]:
                print(time,nei)
                new_time = time+t
                if new_time < min_times[nei]:
                    min_times[nei]=new_time
                    heapq.heappush(q,(min_times[nei],nei))
        max_time = max(min_times)
        return max_time if max_time!=float('inf') else -1