#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        s = str(x)
        n = len(s)
        mid = (n)//2

        left_s  = s[:mid]
        if (n - mid) > mid:
            right_s = s[mid+1:]
        else:
            right_s = s[mid:]
        
        # print(left_s, right_s)

        for i in range(mid):
            # print(left_s[i], right_s[mid-i-1])
            if left_s[i] != right_s[mid-i-1]:
                return False
        return True





if __name__ == "__main__":
    testcases=[
        # (121, True),
        # (-121, False),
        # (10, False),
        # (9, True),
        # (1000, False),
        (1234321, True),
        # (12344321, True),
    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.isPalindrome(testcase[0])
        print(i, 'OK' if ans == testcase[1] else 'Failed', 'expected:%s, return:%s'%(testcase[1], ans))

## Runtime: 176 ms, beat 46.46% of python submissions