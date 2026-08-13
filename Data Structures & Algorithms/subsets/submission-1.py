class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []

        def helper(index):
            if index>=len(nums):
                return
            for ind in range(index+1,len(nums)):
                subset.append(nums[ind])
                res.append(subset.copy())
                helper(ind)
                subset.pop()
        helper(-1)
        return res

