#!/usr/bin/env python3
# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums is None: return 0   # seems not needed
        
        len_nums = len(nums)
        # if len_nums == 0: return 0  # seems not needed

        # print('original:', nums)
        num_set = set()
        removed_count = 0
        for i in range(len_nums-1, -1, -1): # for python2, use xrange
            n = nums[i]
            # print('%d: ' % n, end='')
            if n in num_set:
                # print('removed')
                nums.pop(i)
                removed_count += 1
            else:
                # print('keep')
                num_set.add(n)
        # print('modified:', nums)
        return len_nums - removed_count


if __name__ == "__main__":
    testcases=[
        ([1, 1, 2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5),

    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.removeDuplicates(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 72 ms, faster than 62.11% of Python3 online submissions for Remove Duplicates from Sorted Array.
