#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        tmp_list = []
        negative = x < 0
        x = abs(x)
        if x == 0:
            tmp_list.append(0)
        while x:
            n = x % 10
            x = x // 10
            tmp_list.append(n)

        # print('-' if negative else '+', tmp_list)

        result = 0
        for i, num in enumerate(tmp_list[::-1]):
            result = result + num * (10**i)
            # print(result)

        if negative:
            result = -result

        max_int32 = 2**31 -1
        min_int32 = - max_int32 + 1
        if result > max_int32 -1 or result < min_int32:
            result = 0

        # print('result=', result)
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