# problem link: https://leetcode.com/problems/first-missing-positive/

class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        
        num_dict = dict()
        min_num, max_num = float("inf"), 0
        for n in nums:
            if n < 1:
                continue
            
            num_dict[n] = 1
            if n > max_num: max_num = n
            if n < min_num: min_num = n
        
        if min_num > 1:
            return 1
        
        for i in range(1, max_num + 1):
            if i not in num_dict:
                return i
        
        return max_num + 1
            
        
