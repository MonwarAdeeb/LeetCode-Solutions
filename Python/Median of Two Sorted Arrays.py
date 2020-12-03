import statistics as stat

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        array.sort()
        output = float(stat.median(array))
        return output