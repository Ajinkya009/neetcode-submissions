class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        all_tickets: List[List[str]] = []
        graph = collections.defaultdict(list)

        for u,v in tickets:
            graph[u].append(v)
        for u in graph:
            graph[u].sort()
        def dfs(airport):
            nonlocal tickets
            while graph[airport]:
                dest = graph[airport].pop(0)
                dfs(dest)
            tickets.append(airport)
        
        tickets = []
        dfs("JFK")
        
        return tickets[::-1]