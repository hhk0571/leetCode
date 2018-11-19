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

        return self.reverse(x) == x


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # assumpe x is never a negative number
        if x == 0: return 0
        result = 0
        while x:
            n = x % 10
            x = x // 10
            result = result * 10 + n

        return result



if __name__ == "__main__":
    testcases=[
        (121, True),
        (-121, False),
        (10, False),
    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.isPalindrome(testcase[0])
        print(i, 'OK' if ans == testcase[1] else 'Failed', 'expected:%s, return:%s'%(testcase[1], ans))

## Runtime: 216 ms, beat 20.61% of python submissions