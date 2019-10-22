class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set([e for e in nums if e > 0])
        for i in range(len(nums)):
            if i+1 not in s:
                return i+1
        
        tmp = []
        for num in nums:
            if num > 0 and num not in tmp: # O(n^2)
                tmp.append(num)
                
        if tmp == []:
            return 1
                
        for num in tmp:
            if num < 0:
                num = -num
            if num < len(tmp) + 1:
                tmp[num-1] = -tmp[num-1]
        
        
        
        for idx, num in enumerate(tmp):
            if num > 0:
                return idx + 1
        
        if tmp[0] < 0:
            return len(tmp) + 1
        else:
            return 1