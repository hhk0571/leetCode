#!/usr/bin/env python
# coding: utf-8
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            nums_len = len(nums)
            if target < nums[0]:  return 0
            if target > nums[-1]: return nums_len
            
            # binary search
            ret = 0
            start, end, mid = 0, nums_len-1, 0
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid -1
                else:
                    ret = mid
                    break
            
            if nums[mid] < target:
                mid += 1

            return mid



if __name__ == "__main__":
    testcases=[
        ([[1,3,5,6], 5], 2),
        ([[1,3,5,6], 2], 1),
        ([[1,3,5,6], 7], 4),
        ([[1,3,5,6], 0], 0),
        ([[1,3,5  ], 4], 2)
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.searchInsert(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 20 ms, faster than 100.00% of Python online submissions for Search Insert Position.
