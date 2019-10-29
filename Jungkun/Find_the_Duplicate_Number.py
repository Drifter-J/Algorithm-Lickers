# https://leetcode.com/submissions/detail/274228415/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            if n not in nums_set:
                nums_set.add(n)
            else:
                return n
