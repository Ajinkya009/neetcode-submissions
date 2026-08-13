class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        cand_len = len(candidates)
        current = []

        def helper(index,diff):
            if diff==0:
                result.append(current.copy())
                return
            for ind in range(index,cand_len):
                if ind>index and candidates[ind]==candidates[ind-1]:
                    continue
                remaining = diff - candidates[ind]
                if remaining>=0:
                    current.append(candidates[ind])
                    helper(ind+1,remaining)
                    current.pop()
        
        helper(0,target)

        return result
