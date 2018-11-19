#!/usr/bin/env python3
# coding: utf-8

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # if nums is None: return 0     # seems not needed
    
        len_nums = len(nums)
        # if len_nums == 0: return 0    # seems not needed

        removed_count = 0
        for i in range(len_nums-1, -1, -1): # for python2, use xrange
            n = nums[i]
            if n == val:
                nums.pop(i)
                removed_count += 1

        return len_nums - removed_count


if __name__ == "__main__":
    testcases=[
        ([[0,1,2,2,3,0,4,2], 2], 5),

    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.removeElement(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 40 ms, faster than 71.37% of Python3 online submissions for Remove Element.
