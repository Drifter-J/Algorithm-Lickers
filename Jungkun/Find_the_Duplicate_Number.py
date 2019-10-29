# https://leetcode.com/submissions/detail/274226849/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
            else:
                return nums[i]
