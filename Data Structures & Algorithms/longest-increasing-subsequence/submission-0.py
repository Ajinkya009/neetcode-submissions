class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_len:int = len(nums)
        lis:List[int] = [nums[0]]
        
        for i in range(1,nums_len):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            else:
                low=0
                high=len(lis)-1
                while low<high:
                    mid = low + (high-low)//2
                    if lis[mid]<nums[i]:
                        low=mid+1
                    else:
                        high=mid
                lis[low]=nums[i]
        return len(lis)