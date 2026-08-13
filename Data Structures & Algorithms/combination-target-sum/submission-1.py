class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combinations = []
        #nums.sort()

        def helper(diff,ind):
            if diff==0:
                output.append(combinations.copy())
            
            for index in range(ind,len(nums)):
                remaining = diff - nums[index]
                if remaining>=0:
                    combinations.append(nums[index])
                    helper(remaining,index)
                    combinations.pop()
            
        helper(target,0)
        return output     
        