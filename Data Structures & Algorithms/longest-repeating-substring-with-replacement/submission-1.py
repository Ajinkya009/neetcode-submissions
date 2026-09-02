class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        s_len = len(s)
        freq = defaultdict(int)
        max_freq = 0
        max_len = 0

        while right<s_len:
            freq[s[right]]+=1
            max_freq = max(max_freq,freq[s[right]])
            chars_to_replace = right-left+1 - max_freq
            if chars_to_replace>k:
                freq[s[left]]-=1
                left+=1
            max_len = right - left + 1
            right+=1
        return max_len