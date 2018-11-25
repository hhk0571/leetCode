#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1.0
        
        if n < 0:
            is_n_negative = True
            n = -n
        else:
            is_n_negative = False
        
        result = power(x, n)

        if is_n_negative:
            result = 1/result
        
        return result

def power(x, n):
    if n == 1: return x

    s = power(x, n//2)
    if n % 2 == 0:
        return s * s
    else:
        return s * s * x


if __name__ == "__main__":
    testcases = [
        ([2.0, 10], 1024.0),
        ([2.10000, 3], 9.261000000000001),
        ([2.0, -2], 0.25),
        ([2.1, 0], 1),
        ([0.00001, 2147483647], 0),
    ]
    
    for i, tc in enumerate(testcases):
        solution = Solution()
        ans = solution.myPow(*tc[0])
        print(i, 'OK' if ans == tc[1] else 'Failed', 'expected:%s, return:%s'%(tc[1], ans))

# Runtime: 20 ms, faster than 100.00% of Python online submissions for Pow(x, n).
