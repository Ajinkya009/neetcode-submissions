class Solution:
    def calculate_hours_needed(self,piles,mid,h):
        hours_needed = 0
        for pile in piles:
            hours_needed+=-(-pile//mid)
        return hours_needed

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = 0
        max_pile = 0
        for pile in piles:
            total_bananas+=pile
            max_pile = max(max_pile,pile)
        start = total_bananas//h
        end = max_pile
        min_hours = []
        while start<=end:
            mid = start + (end-start)//2
            if mid==0:
                start+=1
                continue
            hours_needed = self.calculate_hours_needed(piles,mid,h)
            if hours_needed>h:
                start=mid+1
            elif hours_needed<=h:
                end=mid-1
                min_hours.append(mid)
        return min(min_hours)

