# python3
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''
def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    l = m+n

    # m과 n이 둘씩 있을 때 또는 m과 n이 하나씩 있을때 빠르게 끝냄
    if m==2 and n==2:
        return (max(nums1[0], nums2[0]) + min(nums1[m-1], nums2[n-1]))/2
    if m==1 and n==1:
        return (nums1[0] + nums2[0])/2
    
    # 총 길이가 짝수일 때, 홀수일 때 
    if l%2:
        return findKth(nums1, nums2, l//2)
    else:
        return (findKth(nums1, nums2, l//2-1) + findKth(nums1, nums2, l//2))/2.0
    

# 재귀로 풀수 있을꺼라 생각했지만.. 능력 부족으로 이 부분은 인터넷을 참고했습니다.ㅜㅜ
def findKth(nums1, nums2, mid):
    if len(nums2)>len(nums1):
        nums2,nums1=nums1,nums2
    if not nums2:
        return nums1[mid]
    if mid == len(nums1)+len(nums2)-1:
        return max(nums2[-1], nums1[-1])

    i = len(nums2)//2
    j = mid - i

    if nums2[i] > nums1[j]:
        return findKth(nums2[:i], nums1[j:], i)
    else:
        return findKth(nums2[i:], nums1[:j], j)


nums1 = [1,4,9,10]
nums2 = [2,7,8]
print(findMedianSortedArrays(nums1,nums2))
