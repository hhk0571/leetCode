#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    max_int32 =  2147483647 # 2**31 -1
    min_int32 = -2147483648 #-2**31

    nums={
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        num_str = ''
        got_sign = False
        got_num  = False
        negative = False
        for ch in str:
            if ch == ' ':
                if got_num:
                    break
                elif got_sign:
                    return 0
                else:
                    continue
            elif ch in '+-':
                if got_num: break
                if not got_sign:
                    got_sign = True
                    if ch == '-': negative = True
                    continue
                else:
                    return 0
            elif ch in '0123456789':
                num_str += ch
                if not got_num:
                    got_num = True
            else:
                if got_num:
                    break
                else:
                    return 0
        
        result = 0
        for c in num_str:
            result = result * 10 + self.nums[c]
        
        if negative:
            result = -result

        if result > self.max_int32:
            result = self.max_int32
        if result < self.min_int32:
            result = self.min_int32

        return result




if __name__ == "__main__":
    testcases=[
        ('1234', 1234),
        ('+1234', 1234),
        ('-1234', -1234),
        ('      1234', 1234),
        ('      +1234', 1234),
        ('      -1234', -1234),
        ('      a1234', 0),
        ('      1234abc', 1234),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("+91283472332", 2147483647),
        ("4193 with words", 4193),
        ("   +0 123", 0),
        ("0-1", 0),
        ("    -88827   5655  U", -88827),
        ("-5-", -5)

    ]

    solution = Solution()
    for i, testcase in enumerate(testcases):
        ans = solution.myAtoi(testcase[0])
        print(i, 'OK' if ans == testcase[1] else 'Failed', 'str:%s, expected:%s, given:%s'%(testcase[0], testcase[1], ans))

# Runtime: 36 ms, faster than 93.29% of Python online submissions for String to Integer (atoi).
