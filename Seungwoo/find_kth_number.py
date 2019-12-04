class Solution:
    def findKthNumber(self, n, k):
        return self.find_kth_with_prefix(n, k, 1)
    
    def find_kth_with_prefix(self, n, k, prefix = 1):
        
        cur_digit = prefix
        cnt = self.count_prefix(n, k, cur_digit)
        
        if k <= cnt: # ans is btw cur_digit 0 ~ cur_digit 9
            k -= 1
            if k == 0:
                return cur_digit
            cur_digit *= 10
            
            for i in range(10):
                cnt = self.count_prefix(n, k, cur_digit)
                
                if k <= cnt: # recursive call
                    return self.find_kth_with_prefix(n, k, prefix = cur_digit)
                elif k == cnt:
                    return cur_digit
                else:
                    k -= cnt

                cur_digit += 1
        
        else:
            return self.find_kth_with_prefix(n, k - cnt, prefix = cur_digit + 1)
        
    def count_prefix(self, n, k, prefix):
        res = 0 #count for current node
        l = r = prefix
        while l <= n:
            if r <= n:
                res += r - l + 1
            else: # right out of range
                res += max(0,n-l+1)
            l *= 10
            r = r * 10 + 9        
        return res            
        
if __name__ == '__main__':
    s = Solution()
    # print(s.findKthNumber(10000, 10000))
    # print(s.count_prefix(13, 5))
    # print(s.findKthNumber(13,5))
    print(s.findKthNumber(7747794, 5857460))
    
