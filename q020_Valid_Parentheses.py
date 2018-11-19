#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    brackets ={
        '(':')',
        '[':']',
        '{':'}',
    }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i, ch in enumerate(s):
            if ch not in '([{':
                return False
            sub_s = #TODO: implement this method
            


if __name__ == "__main__":
    testcases=[
        ('()' , True ),
        ('()[]{}' , True ),
        ('(]', False),
        ('([)]', False),
        ('{[]}', False),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.isValid(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 24 ms, faster than 86.43% of Python online submissions for Longest Common Prefix.
