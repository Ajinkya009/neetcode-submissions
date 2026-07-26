class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            m = left + (right-left)//2
            if nums[m]<nums[right]:
                right = m
            else:
                left = m+1
        return nums[left]