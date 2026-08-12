class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(min_heap)
        while len(min_heap)>1:
            heavy1,heavy2 = -heapq.heappop(min_heap),-(heapq.heappop(min_heap))
            diff = heavy1-heavy2
            heapq.heappush(min_heap,-(diff))
        return -(min_heap[0]) if len(min_heap)==1 else 0 
