# https://leetcode.com/submissions/detail/274238885/
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longcon = 0
        for n in num_set:
            if n-1 not in num_set:
                temp = n+1
                while temp in num_set:
                    temp+=1
                longcon = max(longcon, temp-n)
        return longcon
