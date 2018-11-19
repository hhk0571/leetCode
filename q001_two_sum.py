#!/usr/bin/env python
# coding: utf-8

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for index_a, a in enumerate(nums):
            b = target - a
            index_b = d.get(b)
            if index_b is not None:
                return [index_b, index_a]
            else:
                d[a]=index_a


if __name__ == "__main__":
    testcases=[
        # nums,           target, expected
        ([2 , 7 , 11 , 15 ], 9  , [0 , 1] ),
        ([3 , 2 , 4       ], 6  , [1 , 2] ),
        ([2 , 5 , 5  , 11 ], 10 , [1 , 2] ),

    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.twoSum(testcase[0], testcase[1])
        print(i, 'OK' if ans == testcase[2] else 'Failed', 'str:%s, expected:%s, return:%s'%(testcase[0], testcase[2], ans))

# Runtime: 24 ms, faster than 87.41% of Python online submissions.
