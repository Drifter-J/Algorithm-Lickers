def binary_search(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1 
        
    if len(nums1) == 0:
        if len(nums2) % 2 == 0:
            return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2])/2
        else:
            return nums2[len(nums2) // 2]
    
    start = 0
    end = len(nums1) 
    
    i = (start + end) // 2 # range from 0 to len(nums1)-1 
    j = (len(nums1) + len(nums2) + 1) // 2 - i 
    
    while start <= end: 
        if i < len(nums1) and nums1[i] < nums2[j-1]:
            # increase i 
            start = i+1 
        elif i > 0 and nums2[j] < nums1[i-1]:
            # decrease i 
            end = i-1 
        else:
            break
        i = (start + end) // 2 # range from 0 to len(nums1)-1 
        j = (len(nums1) + len(nums2) + 1) // 2 - i    

    if i == 0: 
        left = nums2[j-1]
    elif j == 0:
        left = nums1[i-1]
    else:
        left = max(nums1[i-1], nums2[j-1])
        
    if i == len(nums1):
        right = nums2[j]
    elif j == len(nums2):
        right = nums1[i] 
    else:
        right = min(nums1[i], nums2[j])
    

    if (len(nums1) + len(nums2)) % 2 == 0:
        return (left + right) / 2
    else:
        return left
    


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return binary_search(nums1, nums2)