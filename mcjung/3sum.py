# submission link: https://leetcode.com/submissions/detail/261651753/

from collections import defaultdict

class Solution:    
    def search_from_map(self, m, a, b, target):
        if target not in m: 
            return False
        
        cnt = m[target]
        if target in (a, b) and cnt >= 2 and target != 0: 
            return True
        elif target > b or a < target < 0: 
            return True
        else: 
            return False
    
    def parse_array(self, nums):
        m = defaultdict(int)
        pos, neg = [], []
        
        for num in sorted(nums):
            if num >= 0 and (not pos or num != pos[-1]):
                pos.append(num)
            elif not neg or num != neg[-1]: 
                neg.append(num)
            m[num] += 1
            
        return m, pos, neg
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        item_map, pos, neg = self.parse_array(nums)
        
        if 0 in item_map and item_map[0] > 2: 
            result.append([0, 0, 0])
            
        for a in neg:
            for b in pos:
                c = -(a + b)
                if self.search_from_map(item_map, a, b, c):
                    result.append(sorted([a, b, c]))
        
        return sorted(result)
