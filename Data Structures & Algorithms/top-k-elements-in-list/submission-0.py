class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = defaultdict(list)
        max_freq = 0
        for num in nums:
            count[num]+=1
            max_freq = max(max_freq,count[num])
        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(max_freq,0,-1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
                    if len(res)==k:
                        return res
        return []