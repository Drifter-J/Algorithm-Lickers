class Solution:
    def twosum_res(nums, target):
        comp = {}
        res = []
        for idx, elem in enumerate(nums):
            comp[elem] = idx

        for idx, elem in enumerate(nums):

            if target-elem in comp and idx != comp[target-elem]:
                res.append((elem, target-elem))
        if len(res) > 0:
            return res
        else:       
            return -1 
        
    def threeSum(self, nums):
        res = {}
        hist = {}
        
        for num in nums:
            if num in hist:
                hist[num] += 1
            else:
                hist[num] = 1
        
        if len(hist) == 1 and 0 in hist and hist[0] > 2:
            return [[0,0,0]]
        
        for idx, elem in enumerate(nums):
            # print(elem)
            t_sums = Solution.twosum_res(nums[:idx] + nums[idx+1:], -elem)

            if t_sums != -1:

                for t_sum in t_sums:
                    tmp = tuple(sorted([elem, *t_sum]))
                    if tmp not in res:
                        res[tmp] = 1

        return [list(e) for e in res]
    