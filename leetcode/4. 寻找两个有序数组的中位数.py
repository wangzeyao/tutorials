class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        liststack = nums1 + nums2
        liststack.sort()
        if (len(nums1) + len(nums2)) % 2 != 0:
            index = int((len(liststack)-1)/2)
            mid = liststack[index]
            return float(mid)
        else:
            return float((liststack[int(len(liststack)/2)]+liststack[int(len(liststack)/2-1)])/2)

nums1 = [1, 2]
nums2 = [3,5]

sol = Solution()
a = sol.findMedianSortedArrays(nums1,nums2)
print(a)