class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = nums1 + nums2
        combined.sort()
        n = len(combined)
        if n % 2 == 0:
            middle1 = combined[n//2 - 1]
            middle2 = combined[n//2]
            median = (middle1 + middle2) / 2.0
        else:
            median = combined[n//2]
        return median
