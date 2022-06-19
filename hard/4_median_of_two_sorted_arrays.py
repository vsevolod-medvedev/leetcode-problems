"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:
 • nums1.length == m
 • nums2.length == n
 • 0 <= m <= 1000
 • 0 <= n <= 1000
 • 1 <= m + n <= 2000
 • -10^6 <= nums1[i], nums2[i] <= 10^6
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self._merge(nums1, nums2)
        count = len(merged)
        i = count // 2
        if count % 2 == 0:
            return float(merged[i - 1] + merged[i]) / 2
        else:
            return merged[i]

    @staticmethod
    def _merge(nums1: List[int], nums2: List[int]) -> List[int]:
        # Note: Can optimize with merge sort here
        return sorted(nums1 + nums2)


def test():
    solution = Solution()
    for i, test_case in enumerate((
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    )):
        actual = solution.findMedianSortedArrays(nums1=test_case[0], nums2=test_case[1])
        expected = test_case[2]
        assert actual == expected, f"case {i}: expected {expected}, got {actual}"
    print("Test passed!")


test()
