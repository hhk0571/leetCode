#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    max_int32 =  2147483647 # 2**31 -1
    min_int32 = -2147483648 #-2**31

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend == 0 : return 0

        is_negative = not((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0))

        quotient = 0 
        dividend = abs(dividend)
        divisor  = abs(divisor)

        while dividend >= divisor:
            base_quotient = 1
            last_divisor = divisor
            multi_divisor = divisor << 1
            while dividend >= multi_divisor:
                last_divisor = multi_divisor
                multi_divisor = (multi_divisor << 1)
                base_quotient = (base_quotient << 1)

            quotient += base_quotient
            dividend -= last_divisor

        
        if is_negative:
            quotient = -quotient
        
        if quotient > self.max_int32: 
            quotient = self.max_int32
        elif quotient < self.min_int32:
            quotient = self.min_int32

        return quotient



if __name__ == "__main__":
    testcases=[
        ([ 100        ,  3] ,  33         ),
        ([ 7         , -3] , -2          ),
        ([-1         ,  1] , -1          ),
        ([-2147483648, -1] ,  2147483647 ),
    ]

    solution = Solution()
    for i, tc in enumerate(testcases):
        ans = solution.divide(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))


# Runtime: 28 ms, faster than 100.00% of Python online submissions for Divide Two Integers.
