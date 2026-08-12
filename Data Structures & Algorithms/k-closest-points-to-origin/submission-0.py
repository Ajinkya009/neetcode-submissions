class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_index = []
        heapq.heapify(distance_index)
        origin = [0,0]
        for point in points:
            distance = math.dist(origin,point)
            heapq.heappush(distance_index,(-(distance),point[0],point[1]))
            if len(distance_index)>k:
                heapq.heappop(distance_index)
        output = []
        while len(distance_index)>0:
            d_i = heapq.heappop(distance_index)
            output.append([d_i[1],d_i[2]])
        return output