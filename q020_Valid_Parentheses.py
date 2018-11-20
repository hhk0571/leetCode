#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    OPEN_BRACKET ={
        ')':'(',
        ']':'[',
        '}':'{',
    }
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_stack = []
        for ch in s:
            if ch in '([{':
                bracket_stack.append(ch)
            else: # it's close bracket
                open_bracket = self.OPEN_BRACKET[ch]
                stack_top = bracket_stack[-1] if bracket_stack else None
                if stack_top != open_bracket:
                    return False
                else:
                    bracket_stack.pop()
        return bracket_stack == []

if __name__ == "__main__":
    testcases=[
        ('()'     , True  ),
        ('()[]{}' , True  ),
        ('(]'     , False ),
        ('([)]'   , False ),
        ('{[]}'   , True  ),
        (']'      , False ),
        ("["      , False ),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.isValid(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 24 ms, faster than 78.12% of Python online submissions for Valid Parentheses.
