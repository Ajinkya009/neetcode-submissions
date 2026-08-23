class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited: Set[int] = set()
        graph: Dict[List] = collections.defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        def dfs(root,parent):
            if root in visited:
                return False
            visited.add(root)
            for node in graph[root]:
                if node == parent:
                    continue
                if not dfs(node,root):
                    return False
            return True
        
        return dfs(0,-1) and len(visited)==n