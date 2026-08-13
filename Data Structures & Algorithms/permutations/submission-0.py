class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        st = set()

        def helper(base_ind):
            if len(current)==len(nums):
                result.append(current.copy())
                return
            
            for ind in range(len(nums)):
                if ind in st:
                    continue
                current.append(nums[ind])
                st.add(ind)
                helper(ind)
                st.remove(ind)
                current.pop()
        helper(-1)
        return result