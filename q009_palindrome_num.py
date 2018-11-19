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

        for i in range(mid):
            # print(s[i], s[-i-1])
            if s[i] != s[-(i+1)]:
                return False
        return True

if __name__ == "__main__":
    testcases=[
        ( 121     , True ),
        (-121     , False),
        ( 10      , False),
        ( 9       , True ),
        ( 1000    , False),
        ( 1234321 , True ),
        ( 12344321, True ),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.isPalindrome(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

## Runtime: 144 ms, beat 89.41% of python submissions