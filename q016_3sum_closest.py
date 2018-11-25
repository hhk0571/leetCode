#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        nums = sorted(nums)
        min_sum = nums[0] + nums[1] + nums[-1]

        # find all [a, b, c]
        last_a = None
        last_gap = None
        for idx_a in range(nums_len-2):
            a = nums[idx_a]
            if last_a == a: continue
            last_a = a
            idx_b = idx_a + 1
            idx_c = nums_len-1
            benchmark = target - a
            while idx_b < idx_c:
                b = nums[idx_b]
                c = nums[idx_c]
                two_sum = b + c
                gap = abs(two_sum - benchmark)
                if last_gap is None:
                    last_gap = gap
                if gap == 0:
                    return target
                elif last_gap and gap < last_gap:
                    min_sum = a + b + c
                    last_gap = gap

                if two_sum < benchmark: # means b is too small, try bigger one
                    idx_b += 1
                elif two_sum > benchmark: # means c is too large, try smaller one
                    idx_c -= 1

        return min_sum


if __name__ == "__main__":
    testcases = [
        ([[-1, 2, 1, -4], 1], 2),
        ([[0,0,0], 1], 0)
    ]
    
    for i, tc in enumerate(testcases):
        solution = Solution()
        ans = solution.threeSumClosest(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 56 ms, faster than 94.78% of Python online submissions for 3Sum Closest.
