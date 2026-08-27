class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [0]*len(nums)
        max_money = 0
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])

        for ind in range(2,len(nums)):
            dp[ind] = max(dp[ind-1],dp[ind-2]+nums[ind])
        
        return dp[-1]