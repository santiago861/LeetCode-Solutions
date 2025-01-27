import math
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArr = sorted(nums1 + nums2)
        if len(sortedArr) % 2 == 1:
            return sortedArr[int(math.floor(len(sortedArr) / 2))]
        else:
            return (sortedArr[int(len(sortedArr) / 2)] + sortedArr[int((len(sortedArr) / 2) - 1)]) / 2