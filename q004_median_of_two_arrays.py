#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = sorted(nums1 + nums2)
        merged_list_len = len(merged_list)
        half_len = merged_list_len//2

        if (merged_list_len - half_len) > half_len:
            return merged_list[half_len]
        else:
            return (merged_list[half_len -1] + merged_list[half_len])/2.0


if __name__ == "__main__":
    testcases=[
        ([[1, 3], [ 2   ]], 2.0),
        ([[1, 2], [ 3, 4]], 2.5),
        ([[    ], [ 1   ]], 1.0),
        ([[3   ], [-2,-1]], -1.0)

    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.findMedianSortedArrays(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 68 ms, faster than 47.54% of Python online submissions for Median of Two Sorted Arrays.
