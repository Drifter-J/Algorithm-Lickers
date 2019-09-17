class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_map = {}
        
        for i, n in enumerate(nums):
            search_map[n] = i
        
        for i, n in enumerate(nums):
            s = target - n
            
            if s not in search_map: continue
                
            j = search_map[s]
            if i == j: continue
            
            return [i, j] if i < j else [j, i]
