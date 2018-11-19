#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    symbol = {
        'I':    1,
        'V':    5,
        'X':    10,
        'L':    50,
        'C':    100,
        'D':    500,
        'M':    1000,
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result  = 0
        tmp_res = 0
        last_n  = 10000
        for ch in s:
            n = self.symbol.get(ch)
            if n > last_n: # subtraction
                result = result + n - tmp_res - tmp_res
                tmp_res = 0
            else:
                result += n
                tmp_res = n
            last_n = n
        
        return result




if __name__ == "__main__":
    testcases=[
        ('III'    , 3   ),
        ('IV'     , 4   ),
        ('IX'     , 9   ),
        ('XII'    , 12  ),
        ('VIII'   , 8   ),
        ('XXVII'  , 27  ),
        ('LVIII'  , 58  ),
        ('MCMXCIV', 1994),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.romanToInt(tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

## Runtime: 96 ms, beat 47.89% of python submissions