from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

        The overall run time complexity should be O(log (m+n)).
        :param nums1: first array of integers
        :param nums2: seconds array of integers
        :return: the median of the 2 joined arrays
        """
        arr = nums1 + nums2
        arr.sort()

        n = len(arr)

        # If length of array is even
        if n % 2 == 0:
            z = n // 2
            e = arr[z]
            q = arr[z - 1]
            ans = (e + q) / 2
            return ans

        # If length of array is odd
        else:
            z = n // 2
            ans = arr[z]
            return ans
