# https://leetcode.com/submissions/detail/272506543/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=0:
                nums.pop(i)
        for i in range(len(nums)):
            if abs(nums[i])<=len(nums) and nums[abs(nums[i])-1]>0 :
                nums[abs(nums[i])-1] *=-1
        for i in range(len(nums)):
            if nums[i]>0:
                return nums.index(nums[i])+1
        return len(nums)+1
