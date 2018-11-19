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
        # args                      expected
        ([[2 , 7 , 11 , 15 ], 9 ] , [0 , 1] ),
        ([[3 , 2 , 4       ], 6 ] , [1 , 2] ),
        ([[2 , 5 , 5  , 11 ], 10] , [1 , 2] ),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.twoSum(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 24 ms, faster than 87.41% of Python online submissions.
