class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_deg = [0]*numCourses
        adj_list = collections.defaultdict(list)
        order = []
        total_courses = 0
        for u,v in prerequisites:
            adj_list[v].append(u)
            in_deg[u]+=1
        
        q = deque(v for v in range(numCourses) if in_deg[v]==0)
        total_courses = len(q)
        while q:
            course = q.popleft()
            order.append(course)
            for c in adj_list[course]:
                in_deg[c]-=1
                if in_deg[c]==0:
                    q.append(c)
                    total_courses+=1
        return order if total_courses==numCourses else []