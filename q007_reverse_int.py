#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    max_int32 =  2147483647 # 2**31 -1
    min_int32 = -2147483648 #-2**31
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        result = 0
        if x < 0:
            negative = True
            x = -x
        else:
            negative = False

        while x:
            n = x % 10
            x = x // 10
            result = result * 10 + n

        if negative:
            result = -result

        if result > self.max_int32 or result < self.min_int32:
            result = 0

        #print('result=', result)
        return result


if __name__ == "__main__":
    tests = {
        0:0,
        123:321,
        -123:-321,
        120:21,
        1534236469:0
    }

    solution = Solution()
    for test in tests:
        ans = solution.reverse(test)
        print(test, ans, 'OK' if ans == tests[test] else 'Failed')