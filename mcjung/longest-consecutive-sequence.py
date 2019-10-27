# problem link: https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        
        for num in nums:
            num_set.add(num)
        
        max_len = 0
        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                continue
                
            tot_len = 1
            
            first = num - 1
            last = num + 1
            while True:
                if first in num_set:
                    num_set.remove(first)
                    first -= 1
                elif last in num_set:
                    num_set.remove(last)
                    last += 1
                else:
                    break
                tot_len += 1
                
            max_len = max(max_len, tot_len)
        
        return max_len
            
                
            
        
        
