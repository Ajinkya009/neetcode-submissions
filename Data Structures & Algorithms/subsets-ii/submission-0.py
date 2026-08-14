class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        current = []
        result = []
        def helper(base_index):
            result.append(current.copy())
            for ind in range(base_index,nums_len):
                if ind>base_index and nums[ind]==nums[ind-1]:
                    continue
                current.append(nums[ind])
                helper(ind+1)
                current.pop()
        helper(0)
        return result
