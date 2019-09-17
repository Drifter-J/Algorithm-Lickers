class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            comp = {}
    
            for idx, elem in enumerate(nums):
                comp[elem] = idx

            for idx, elem in enumerate(nums):
                if target-elem in comp and idx != comp[target-elem]:
                    return idx, comp[target-elem]
            return -1