#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        n = len(s)
        start_index=0
        end_index =0
        for i in range(n):
            for j in range(i+1, n+1):
                if self.all_unique(s, i, j):
                    new_len = j -i
                    if new_len > answer:
                        answer = new_len
                        start_index = i
                        end_index = j
        print('str:%s, substr:%s, len:%d, start:%d, end:%d' %(s, s[start_index:end_index], answer, start_index, end_index))
        return answer
    
    @staticmethod
    def all_unique(s, start, end):
        c_set = set()
        for i in range(start, end):
            ch = s[i]
            if ch in c_set:
                return False
            c_set.add(ch)
        return True


if __name__ == "__main__":
    tests = {
        "abcabcbb":3,
        "bbbbb":1,
        "pwwkew":3,
        "pxckicaghufczmaccgwigmrqcteqkbwbaamicoqlivnjjoomwkucznvdgztqarsargkwuaheyvohle":11,
    }

    solution = Solution()
    for test in tests:
        print(test, tests[test], solution.lengthOfLongestSubstring(test))


# HHK@HHKPC MINGW64 /d/test/python
# $ python problem03_1.py
# str:abcabcbb, substr:abc, len:3, start:0, end:3
# abcabcbb 3 3
# str:bbbbb, substr:b, len:1, start:0, end:1
# bbbbb 1 1
# str:pwwkew, substr:wke, len:3, start:2, end:5
# pwwkew 3 3
# str:pxckicaghufczmaccgwigmrqcteqkbwbaamicoqlivnjjoomwkucznvdgztqarsargkwuaheyvohle, substr:omwkucznvdg, len:11, start:46, end:57
# pxckicaghufczmaccgwigmrqcteqkbwbaamicoqlivnjjoomwkucznvdgztqarsargkwuaheyvohle 11 11
