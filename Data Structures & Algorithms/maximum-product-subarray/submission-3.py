class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = max_so_far
        for i in range(1,len(nums)):
            max_temp = max_so_far*nums[i]
            min_temp = min_so_far*nums[i]
            max_so_far = max(nums[i],max_temp,min_temp)
            min_so_far = min(nums[i],max_temp,min_temp)
            res = max(res,max_so_far)
        return res