class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            count = [0]*26
            for alphabet in string:
                count[ord(alphabet)-ord('a')]+=1
            res[tuple(count)].append(string)
        return list(res.values())