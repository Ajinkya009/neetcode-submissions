class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        max_len = 0
        l = 0
        left = 0
        s = set()
        
        for r in range(len(st)):
            while st[r] in s:
                s.remove(st[l])
                l+=1
            s.add(st[r])
            max_len = max(max_len,r-l+1)
        return max_len