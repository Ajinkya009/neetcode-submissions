class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        all_tickets: List[List[str]] = []
        graph = collections.defaultdict(list)

        for u,v in sorted(tickets)[::-1]:
            graph[u].append(v)

        def dfs(airport):
            nonlocal tickets
            while graph[airport]:
                dest = graph[airport].pop()
                dfs(dest)
            tickets.append(airport)
        
        tickets = []
        dfs("JFK")
        
        return tickets[::-1]