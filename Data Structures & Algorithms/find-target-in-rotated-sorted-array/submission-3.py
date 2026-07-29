class Solution:
    def binary_search(self,nums,left,right,target):
        print(left,right)
        while left<=right:
            m = (left+right)//2
            print(m,nums[m])
            if nums[m]==target: return m
            elif nums[m]>target:
                right=m-1
            else:
                left=m+1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1

        while left<right:
            m = (left+right)//2
            if nums[m]>nums[right]:
                left = m+1
            else:
                right = m
        pivot = left

        if nums[pivot]<=target<=nums[-1]:
            return self.binary_search(nums,pivot,len(nums)-1,target)
        else:
            return self.binary_search(nums,0,pivot-1,target)