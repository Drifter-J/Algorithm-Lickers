# problem link: https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def next_node(x):
            return nums[x]
        last = self.floyd(next_node, 0)
        return nums[last]
    
    def floyd(self, f, x0):
        tortoise = f(x0)
        hare = f(f(x0))
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(f(hare))

        tortoise = x0
        last_tortoise = None
        while tortoise != hare:
            last_tortoise = tortoise
            tortoise = f(tortoise)
            hare = f(hare)
        

        return last_tortoise
    
        
