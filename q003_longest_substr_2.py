#!/usr/bin/env python
# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)
        if n == 1:
            return 1

        win_str = ''
        # start_index = 0
        # end_index = 0
        for win_size in range(len(set(s))+1, 0, -1):
            for i in range(n): # start index
                win_str = s[i:win_size+i]
                len_set_str = len(set(win_str))
                if len_set_str == win_size:
                    # start_index = i
                    # end_index = win_size+i
                    # print('len:%d, start:%d, end:%d' %(win_size, start_index, end_index))
                    return win_size
        return win_size


if __name__ == "__main__":
    with open('q003_longtext.txt') as f:
        longtext = f.read()
    tests = {
        "abcabcbb":3,
        "bbbbb":1,
        "pwwkew":3,
        "a":1,
        "au":2,
        "pxckicaghufczmaccgwigmrqcteqkbwbaamicoqlivnjjoomwkucznvdgztqarsargkwuaheyvohle":11,
        longtext:95,

    }

    solution = Solution()
    for test in tests:
        # print(test, tests[test], solution.lengthOfLongestSubstring(test))
        print(tests[test], solution.lengthOfLongestSubstring(test))
