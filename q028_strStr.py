#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        
        len_haystack = len(haystack)

        for i in range(len_haystack - len_needle + 1):
            substr = haystack[i:i+len_needle]
            if substr == needle:
                return i
        return -1



if __name__ == "__main__":
    testcases=[
        (['hello'  , 'll'  ] ,  2 ),
        (['aaaaa'  , 'bba' ] , -1 ),
        (['abcded' , ''    ] ,  0 ),
        (['a'      , 'a'   ] ,  0 ),
        (["mississippi", "pi"], 9),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.strStr(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 20 ms, faster than 100.00% of Python online submissions for Implement strStr().
